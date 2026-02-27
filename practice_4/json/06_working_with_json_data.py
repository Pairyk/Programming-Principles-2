import json
import os
from collections import defaultdict
from datetime import datetime

# Inline dataset simulating a real API payload — no file dependency
RAW = '''
{
    "report": "Q2-2024",
    "generated": "2024-07-01T09:00:00",
    "records": [
        {"id": 1,  "region": "EMEA", "product": "CoreDB",  "revenue": 45200, "units": 120, "active": true,
         "tags": ["database", "core"], "rep": {"name": "Alice", "tier": "senior"}},
        {"id": 2,  "region": "APAC", "product": "CoreDB",  "revenue": 31000, "units": 95,  "active": true,
         "tags": ["database", "core"], "rep": {"name": "Ben",   "tier": "junior"}},
        {"id": 3,  "region": "EMEA", "product": "AnalytX", "revenue": 72400, "units": 55,  "active": true,
         "tags": ["analytics", "premium"], "rep": {"name": "Carol", "tier": "senior"}},
        {"id": 4,  "region": "AMER", "product": "AnalytX", "revenue": 18000, "units": 30,  "active": false,
         "tags": ["analytics"], "rep": {"name": "Dave",  "tier": "junior"}},
        {"id": 5,  "region": "APAC", "product": "StreamIO","revenue": 52100, "units": 210, "active": true,
         "tags": ["streaming", "core"], "rep": {"name": "Eve",   "tier": "senior"}},
        {"id": 6,  "region": "AMER", "product": "StreamIO","revenue": 63800, "units": 180, "active": true,
         "tags": ["streaming"], "rep": {"name": "Frank", "tier": "senior"}},
        {"id": 7,  "region": "EMEA", "product": "StreamIO","revenue": 29500, "units": 88,  "active": false,
         "tags": ["streaming", "core"], "rep": {"name": "Grace", "tier": "junior"}},
        {"id": 8,  "region": "AMER", "product": "CoreDB",  "revenue": 41000, "units": 140, "active": true,
         "tags": ["database"], "rep": {"name": "Hank",  "tier": "senior"}}
    ]
}
'''

try:
    data = json.loads(RAW)
except json.JSONDecodeError as e:
    print(f"Fatal parse error: {e}")
    raise SystemExit(1)

records = data["records"]

# --- Example 1: Filter — active senior-rep records above revenue threshold ---
threshold = 40000
top_active = [
    r for r in records
    if r["active"]
    and r["rep"]["tier"] == "senior"
    and r["revenue"] >= threshold
]
print("Top active senior records:")
for r in top_active:
    print(f"  [{r['region']}] {r['product']} — ${r['revenue']:,} ({r['rep']['name']})")

# --- Example 2: Group and aggregate revenue by region ---
region_revenue: dict = defaultdict(float)
region_units:   dict = defaultdict(int)

for r in records:
    region_revenue[r["region"]] += r["revenue"]
    region_units[r["region"]]   += r["units"]

region_summary = [
    {
        "region":      region,
        "total_rev":   region_revenue[region],
        "total_units": region_units[region],
        # Revenue per unit rounded to 2 decimal places
        "rev_per_unit": round(region_revenue[region] / region_units[region], 2)
    }
    for region in sorted(region_revenue)
]
print("\nRegion Summary:")
print(json.dumps(region_summary, indent=2))

# --- Example 3: Map — normalize and reshape records ---
def reshape(r: dict) -> dict:
    return {
        "id":         r["id"],
        "key":        f"{r['region']}::{r['product']}",
        "revenue_k":  round(r["revenue"] / 1000, 1),
        "rep_name":   r["rep"]["name"],
        "is_premium": "premium" in r.get("tags", [])
    }

reshaped = list(map(reshape, records))
print("\nReshaped Records:")
for item in reshaped:
    print(f"  {item['key']:<22} ${item['revenue_k']}k  premium={item['is_premium']}")

# --- Example 4: Aggregate — product-level stats with tag index ---
product_stats: dict = defaultdict(lambda: {"revenue": 0, "units": 0, "count": 0, "tags": set()})

for r in records:
    p = r["product"]
    product_stats[p]["revenue"] += r["revenue"]
    product_stats[p]["units"]   += r["units"]
    product_stats[p]["count"]   += 1
    product_stats[p]["tags"].update(r.get("tags", []))

# Sets are not JSON-serializable — convert before dumping
product_report = {
    prod: {**stats, "tags": sorted(stats["tags"])}
    for prod, stats in product_stats.items()
}
print("\nProduct Stats:")
print(json.dumps(product_report, indent=2))

# --- Example 5: Rank products by revenue and serialize to file ---
ranked = sorted(
    [{"product": p, **{k: v for k, v in s.items() if k != "tags"}, "tags": sorted(s["tags"])}
     for p, s in product_stats.items()],
    key=lambda x: x["revenue"],
    reverse=True
)
OUTPUT_DIR = "practice_4/json/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
out_path = os.path.join(OUTPUT_DIR, "product_ranking.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"report": data["report"], "rankings": ranked}, f, indent=2)
print(f"\nRanking written to: {out_path}")

# --- Example 6: Cross-filter — reps with multi-region presence ---
from collections import defaultdict as dd
rep_regions: dict = dd(set)
for r in records:
    rep_regions[r["rep"]["name"]].add(r["region"])

multi_region_reps = {
    rep: sorted(regions)
    for rep, regions in rep_regions.items()
    if len(regions) > 1
}
print("\nMulti-region reps:", multi_region_reps if multi_region_reps else "None in this dataset")

# --- Example 7: Detect schema anomalies in the dataset ---
RECORD_SCHEMA = {"id", "region", "product", "revenue", "units", "active", "tags", "rep"}
anomalies = [
    {"id": r.get("id"), "missing": sorted(RECORD_SCHEMA - r.keys())}
    for r in records
    if not RECORD_SCHEMA.issubset(r.keys())
]
if anomalies:
    print(f"\nSchema anomalies found: {json.dumps(anomalies, indent=2)}")
else:
    print("\nAll records passed schema validation.")