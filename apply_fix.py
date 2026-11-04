import json, sys
f = json.load(sys.stdin)
with open(f["path"], "rb") as fh:
    data = fh.read()
s, e = f["start"]["offset"], f["end"]["offset"]
data = data[:s] + f["fix"].encode() + data[e:]
with open(f["path"], "wb") as fh:
    fh.write(data)
