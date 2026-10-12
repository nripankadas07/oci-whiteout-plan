from pathlib import PurePosixPath

def run(data):
    layers = data.get("layers")
    if not isinstance(layers, list) or len(layers) > 64:
        raise ValueError("layers must be a list of at most 64 path lists")
    state, trace = {}, []
    for li, entries in enumerate(layers):
        if not isinstance(entries, list) or len(entries) > 10000:
            raise ValueError("each layer needs at most 10000 entries")
        checked = []
        seen = set()
        for entry in entries:
            if not isinstance(entry, dict) or set(entry) != {"path", "kind"}:
                raise ValueError("entry fields: path, kind")
            path, kind = entry["path"], entry["kind"]
            if not isinstance(path, str) or not path or len(path)>4096 or path.startswith("/") or "\\" in path or any(p in ("", ".", "..") for p in path.split("/")) or any(ord(c)<32 for c in path):
                raise ValueError("canonical relative POSIX path required")
            if path in seen or kind not in ("file", "dir"):
                raise ValueError("duplicate path or unsupported kind")
            seen.add(path)
            checked.append((path, kind))
        lower = dict(state)
        for path, kind in checked:
            p = PurePosixPath(path)
            if not p.name.startswith(".wh."):
                continue
            if kind != "file":
                raise ValueError("whiteout markers must be files")
            parent = "" if str(p.parent)=="." else str(p.parent)
            if p.name == ".wh..wh..opq":
                prefix = parent + "/" if parent else ""
                victims = [x for x in lower if x.startswith(prefix) and x != parent]
            else:
                suffix = p.name[4:]
                if suffix in ("", ".", "..") or suffix.startswith(".wh."):
                    raise ValueError("unsupported whiteout basename")
                target = (parent + "/" if parent else "") + suffix
                victims = [x for x in lower if x == target or x.startswith(target+"/")]
            for victim in victims:
                state.pop(victim, None)
            trace.append({"layer":li,"marker":path,"removed":sorted(victims)})
        for path, kind in sorted(checked, key=lambda x:(x[0].count("/"), x[0])):
            if PurePosixPath(path).name.startswith(".wh."):
                continue
            parts = path.split("/")
            for end in range(1,len(parts)):
                parent = "/".join(parts[:end])
                if parent in state and state[parent]["kind"] != "dir":
                    raise ValueError("file used as parent; normalize layer first")
                state.setdefault(parent,{"kind":"dir","layer":li,"implicit":True})
            if kind == "file":
                for victim in list(state):
                    if victim.startswith(path+"/"):
                        del state[victim]
            state[path] = {"kind":kind,"layer":li,"implicit":False}
    return {"paths":dict(sorted(state.items())),"whiteouts":trace}
