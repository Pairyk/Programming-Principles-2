import json
import os
import math
from datetime import datetime

OUTPUT_DIR = "practice_4/json/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Example 1: sqrt / ceil / floor on engineering measurements JSON ---
raw_specs = '''
{
    "project": "BridgeLoad-9B",
    "units": "metric",
    "members": [
        {"id": "M01", "force_kN": 150.0,  "length_m": 6.25,  "material": "steel"},
        {"id": "M02", "force_kN": 340.8,  "length_m": 8.00,  "material": "steel"},
        {"id": "M03", "force_kN": 72.5,   "length_m": 3.75,  "material": "alloy"},
        {"id": "M04", "force_kN": 512.0,  "length_m": 12.50, "material": "steel"},
        {"id": "M05", "force_kN": 198.3,  "length_m": 7.10,  "material": "alloy"}
    ],
    "safety_factor": 1.75
}
'''

try:
    specs = json.loads(raw_specs)
except json.JSONDecodeError as e:
    raise SystemExit(f"Spec parse error at line {e.lineno}: {e.msg}")

sf = specs["safety_factor"]

# sqrt of force gives RMS-style stress index; ceil/floor used for material ordering
analysis = [
    {
        "id":             m["id"],
        "force_kN":       m["force_kN"],
        "stress_index":   round(math.sqrt(m["force_kN"]), 4),
        # ceil ensures we never under-order materials (always round up for safety)
        "units_required": math.ceil(m["length_m"] * sf),
        # floor gives minimum theoretical units (lower bound reference)
        "units_min":      math.floor(m["length_m"]),
        "material":       m["material"]
    }
    for m in specs["members"]
]

print(f"Project: {specs['project']}")
for a in analysis:
    print(f"  {a['id']}  stress={a['stress_index']:.2f}  "
          f"order={a['units_required']} units  (floor={a['units_min']})")

# --- Example 2: sin / cos for geospatial distance (Haversine) in JSON ---
raw_waypoints = '''
{
    "route": "TransAtlantic-7",
    "waypoints": [
        {"name": "New York",   "lat": 40.7128,  "lon": -74.0060},
        {"name": "Reykjavik",  "lat": 64.1355,  "lon": -21.8954},
        {"name": "London",     "lat": 51.5074,  "lon":  -0.1278}
    ]
}
'''

try:
    route_data = json.loads(raw_waypoints)
except json.JSONDecodeError as e:
    raise SystemExit(f"Route parse error: {e.msg}")

EARTH_RADIUS_KM = 6371.0

def haversine(p1: dict, p2: dict) -> float:
    # Convert degrees to radians — required for math trig functions
    lat1, lon1 = math.radians(p1["lat"]), math.radians(p1["lon"])
    lat2, lon2 = math.radians(p2["lat"]), math.radians(p2["lon"])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Haversine formula: a = sin²(Δlat/2) + cos(lat1)·cos(lat2)·sin²(Δlon/2)
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    return round(2 * EARTH_RADIUS_KM * math.asin(math.sqrt(a)), 1)

waypoints = route_data["waypoints"]
legs = [
    {
        "from": waypoints[i]["name"],
        "to":   waypoints[i + 1]["name"],
        "dist_km": haversine(waypoints[i], waypoints[i + 1])
    }
    for i in range(len(waypoints) - 1)
]
total_km = sum(leg["dist_km"] for leg in legs)

print(f"\nRoute: {route_data['route']}")
for leg in legs:
    print(f"  {leg['from']:<14} → {leg['to']:<14}  {leg['dist_km']:>7,.1f} km")
print(f"  {'TOTAL':<30}  {total_km:>7,.1f} km")

# --- Example 3: pi and e in physics / finance calculations ---
raw_physics = '''
{
    "experiments": [
        {"label": "Pendulum Period",  "type": "pendulum", "length_m": 2.5},
        {"label": "Circular Area",   "type": "circle",   "radius_m": 4.0},
        {"label": "Compound Decay",  "type": "decay",    "half_life_s": 300, "elapsed_s": 900}
    ]
}
'''

try:
    physics = json.loads(raw_physics)
except json.JSONDecodeError as e:
    physics = {"experiments": []}

results = []
for exp in physics["experiments"]:
    if exp["type"] == "pendulum":
        # T = 2π√(L/g) — period of a simple pendulum
        period = 2 * math.pi * math.sqrt(exp["length_m"] / 9.81)
        results.append({"label": exp["label"], "result": round(period, 4), "unit": "s"})

    elif exp["type"] == "circle":
        # Area = πr² — precise with math.pi vs 3.14159
        area = math.pi * exp["radius_m"] ** 2
        results.append({"label": exp["label"], "result": round(area, 4), "unit": "m²"})

    elif exp["type"] == "decay":
        # N(t) = N₀ · e^(−λt), where λ = ln2 / half_life
        lam = math.log(2) / exp["half_life_s"]
        # math.e** would work but math.exp() is more numerically stable
        remaining = math.exp(-lam * exp["elapsed_s"])
        results.append({"label": exp["label"], "result": round(remaining, 6), "unit": "fraction remaining"})

print("\nPhysics Results:")
for r in results:
    print(f"  {r['label']:<22}  {r['result']}  {r['unit']}")

# --- Example 4: log / log10 for signal processing on sensor JSON ---
raw_signals = '''
{
    "channel": "RF-monitoring",
    "samples": [
        {"id": "S1", "power_mW": 0.001},
        {"id": "S2", "power_mW": 0.010},
        {"id": "S3", "power_mW": 0.100},
        {"id": "S4", "power_mW": 1.000},
        {"id": "S5", "power_mW": 10.000}
    ]
}
'''

try:
    signals = json.loads(raw_signals)
except json.JSONDecodeError as e:
    signals = {"samples": []}

# dBm = 10 · log10(P_mW / 1mW) — logarithmic scale for signal power
dbm_readings = [
    {
        "id":       s["id"],
        "power_mW": s["power_mW"],
        "dBm":      round(10 * math.log10(s["power_mW"]), 2)
    }
    for s in signals["samples"]
    if s["power_mW"] > 0  # guard: log is undefined for zero/negative
]

print(f"\nChannel: {signals['channel']}")
for r in dbm_readings:
    print(f"  {r['id']}: {r['power_mW']:.3f} mW  →  {r['dBm']:>6.1f} dBm")

# --- Example 5: Assemble and persist the full math analysis ---
output = {
    "generated_at":       datetime.now().isoformat(),
    "constants":          {"pi": math.pi, "e": math.e},
    "bridge_analysis":    analysis,
    "route_legs":         legs,
    "route_total_km":     total_km,
    "physics_results":    results,
    "signal_dbm":         dbm_readings
}

out_path = os.path.join(OUTPUT_DIR, "math_module_results.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
print(f"\nFull analysis written → {out_path}")