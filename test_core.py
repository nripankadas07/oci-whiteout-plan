import json, os, pathlib, subprocess, sys, tempfile, unittest
from oci_whiteout_plan.core import run

CASES = [({'layers': []}, {'paths': {}, 'whiteouts': []}), ({'layers': [[{'path': 'a', 'kind': 'file'}], [{'path': '.wh.a', 'kind': 'file'}]]}, {'paths': {}}), ({'layers': [[{'path': 'a', 'kind': 'file'}], [{'path': '.wh.a', 'kind': 'file'}, {'path': 'a', 'kind': 'file'}]]}, {'paths': {'a': {'kind': 'file', 'layer': 1, 'implicit': False}}}), ({'layers': [[{'path': 'a', 'kind': 'file'}], [{'path': 'a', 'kind': 'file'}, {'path': '.wh.a', 'kind': 'file'}]]}, {'paths': {'a': {'kind': 'file', 'layer': 1, 'implicit': False}}}), ({'layers': [[{'path': 'd/a', 'kind': 'file'}, {'path': 'other', 'kind': 'file'}], [{'path': 'd/.wh..wh..opq', 'kind': 'file'}, {'path': 'd/new', 'kind': 'file'}]]}, 'opaque'), ({'layers': [[{'path': 'd/a', 'kind': 'file'}], [{'path': 'd', 'kind': 'file'}]]}, {'paths': {'d': {'kind': 'file', 'layer': 1, 'implicit': False}}}), ({'layers': [[{'path': '../a', 'kind': 'file'}]]}, 'error'), ({'layers': [[{'path': '/a', 'kind': 'file'}]]}, 'error'), ({'layers': [[{'path': 'a', 'kind': 'file'}, {'path': 'a', 'kind': 'file'}]]}, 'error'), ({'layers': [[{'path': '.wh...', 'kind': 'file'}]]}, 'error'), ({'layers': [[{'path': 'a', 'kind': 'file'}, {'path': 'a/b', 'kind': 'file'}]]}, 'error'), ({'layers': [[{'path': '.wh.a', 'kind': 'dir'}]]}, 'error')]

class ContractTests(unittest.TestCase):
    def test_cli_demo(self):
        r=subprocess.run([sys.executable,"-c","from oci_whiteout_plan.cli import main; raise SystemExit(main())","example.json"],text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIsInstance(json.loads(r.stdout),dict)

    def test_cli_malformed(self):
        with tempfile.TemporaryDirectory() as d:
            path=pathlib.Path(d)/"bad.json";path.write_text("[broken")
            r=subprocess.run([sys.executable,"-c","from oci_whiteout_plan.cli import main; raise SystemExit(main())",str(path)],text=True,capture_output=True)
            self.assertEqual(r.returncode,2)
            self.assertEqual(r.stdout,"")
            self.assertIn("input error",r.stderr)

def make_case(data,expected):
    def test(self):
        before=json.dumps(data,sort_keys=True)
        if expected=="error":
            with self.assertRaises(ValueError): run(data)
        else:
            result=run(data)
            if expected=="opaque":
                self.assertEqual(set(result["paths"]),{"d","d/new","other"})
                self.assertEqual(result["whiteouts"][0]["removed"],["d/a"])
            elif expected=="order":
                self.assertEqual([r["start"] for r in result["requests"]],[50,0])
                self.assertEqual(result["coverage"],[[0,9],[50,59]])
            else:
                for key,value in expected.items(): self.assertEqual(result[key],value)
        self.assertEqual(json.dumps(data,sort_keys=True),before,"input mutated")
    return test
for i,(data,expected) in enumerate(CASES):
    setattr(ContractTests,"test_contract_%02d"%i,make_case(data,expected))

if __name__=="__main__": unittest.main()
