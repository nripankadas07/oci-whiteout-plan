# Synthetic demo

Use the installed command with `example.json`; the expected deterministic output is:

```json
{
  "paths": {
    "etc": {
      "implicit": true,
      "kind": "dir",
      "layer": 0
    },
    "etc/new": {
      "implicit": false,
      "kind": "file",
      "layer": 1
    }
  },
  "whiteouts": [
    {
      "layer": 1,
      "marker": "etc/.wh..wh..opq",
      "removed": [
        "etc/keep",
        "etc/old"
      ]
    }
  ]
}
```

This proves the documented example only, not production efficacy or adoption.
