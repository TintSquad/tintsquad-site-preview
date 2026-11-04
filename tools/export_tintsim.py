#!/usr/bin/env python3
"""Rebuild public/tint-simulator/data.json from Airtable base "Window Tint Simulator".
Run nightly (or before a deploy):  AIRTABLE_TOKEN=... python3 tools/export_tintsim.py && git commit -am 'refresh tint data' && git push
Read-only against Airtable."""
import os, json, urllib.request, urllib.parse, collections
B = "appaIrgW3QJHJ5zqF"; CLIENT = "rec9NqKUFK6BFsaF1"  # Tint Squad
TOK = os.environ.get("AIRTABLE_TOKEN") or os.environ["AIRTABLE_TEST_PAT"]
H = {"Authorization": "Bearer " + TOK}
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=H)))
def rows(t, fields):
    out, off = [], None
    while True:
        q = [("pageSize", "100")] + [("fields[]", f) for f in fields] + ([("offset", off)] if off else [])
        r = get(f"https://api.airtable.com/v0/{B}/{t}?" + urllib.parse.urlencode(q))
        out += r["records"]; off = r.get("offset")
        if not off: return out
tidy = lambda s: " ".join(str(s or "").replace("_", " ").split())
veh = collections.defaultdict(lambda: collections.defaultdict(list))
for r in rows("tblGUHzW2Vp7kzyXN", ["Make", "Model", "Body Style"]):
    f = r["fields"]
    if not f.get("Make") or not f.get("Model"): continue
    veh[tidy(f["Make"])][tidy(f["Model"])].append([r["id"], tidy(f.get("Body Style"))])
cols = collections.defaultdict(list)
for r in sorted(rows("tblMqgQPEiGtwj0hp", ["Color", "Make", "Position"]), key=lambda r: r["fields"].get("Position", 9e9)):
    f = r["fields"]
    if f.get("Color"): cols[tidy(f.get("Make")) or "*"].append([r["id"], tidy(f["Color"])])
cl = get(f"https://api.airtable.com/v0/{B}/tbluiJ7AqIXQOPbbL/{CLIENT}")["fields"]
meta = get(f"https://api.airtable.com/v0/meta/bases/{B}/tables")
years = next(fl["options"]["choices"] for t in meta["tables"] if t["name"] == "Leads & Submissions" for fl in t["fields"] if fl["name"] == "Year")
excluded = [m for m in cl.get("Excluded Makes", []) if m != "None"]
data = {
  "years": sorted([c["name"] for c in years], reverse=True),
  "vehicles": {mk: dict(sorted(v.items())) for mk, v in sorted(veh.items()) if mk not in excluded},
  "colors": dict(cols),
  "shades": {"front": cl.get("Side Front Windows", []), "rear": cl.get("Side Rear Windows", []),
             "back": cl.get("Rear Windshield", []), "full": cl.get("Full Front Windshield", [])},
}
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "public", "tint-simulator", "data.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(data, open(out, "w"), separators=(",", ":"))
print("makes", len(data["vehicles"]), "vehicles", sum(len(b) for m in data["vehicles"].values() for b in m.values()),
      "color makes", len(data["colors"]), "bytes", os.path.getsize(out))
