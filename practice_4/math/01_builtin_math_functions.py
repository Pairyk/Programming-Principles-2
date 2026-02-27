import json
import os
import math
from datetime import datetime

OUTPUT_DIR = "practice_4/json/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Example 1: min/max over deeply nested sensor payload ---
raw_sensor = '''
{
    "station": "AWS-7",
    "location": {"lat": 51.5074, "lon": -0.1278, "elevation_m": 24},
    "readings": [
        {"ts": "2024-01-01T08:00:00", "temp": 3.2,  "humidity": 78, "pressure": 1012.4},
        {"ts": "2024-01-01T09:00:00", "temp": 5.1,  "humidity": 74, "pressure": 1011.8},
        {"ts": "2024-01-01T10:00:00", "temp": 7.8,  "humidity": 69, "pressure": 1010.2},
        {"ts": "2024-01-01T11:00:00", "temp": -1.3, "humidity": 91, "pressure": 1009.5},
        {"ts": "2024-01-01T12:00:00", "temp": 9.4,  "humidity": 65, "pressure": 1008.1}
    ]
}
'''

try:
    sensor = json.loads(raw_sensor)
except json.JSONDecodeError as e:
    print(f"Parse error at line {e.lineno}: {e.msg}")
    raise SystemExit(1)

temps = [r["temp"] for r in sensor["readings"]]
pressures = [r["pressure"] for r in sensor["readings"]]

# min/max with key= lets us pull the full record, not just the value
coldest = min(sensor["readings"], key=lambda r: r["temp"])
hottest = max(sensor["readings"], key=lambda r: r["temp"])

print(f"Station : {sensor['station']}")
print(f"Temp range : {min(temps):.1f}°C  →  {max(temps):.1f}°C")
print(f"Coldest : {coldest['ts']}  ({coldest['temp']}°C)")
print(f"Hottest : {hottest['ts']}  ({hottest['temp']}°C)")
print(f"Pressure span: {max(pressures) - min(pressures):.1f} hPa")

# --- Example 2: abs() for deviation analysis on financial JSON ---
raw_portfolio = '''
{
    "portfolio": "Growth-A",
    "benchmark_return_pct": 8.5,
    "holdings": [
        {"ticker": "AAPL", "weight": 0.25, "return_pct": 12.4},
        {"ticker": "MSFT", "weight": 0.20, "return_pct": 9.1},
        {"ticker": "TSLA", "weight": 0.15, "return_pct": -4.7},
        {"ticker": "NVDA", "weight": 0.25, "return_pct": 31.2},
        {"ticker": "META", "weight": 0.15, "return_pct": 6.3}
    ]
}
'''

try:
    portfolio = json.loads(raw_portfolio)
except json.JSONDecodeError as e:
    print(f"Portfolio parse error: {e.msg}")
    portfolio = {"holdings": [], "benchmark_return_pct": 0}

benchmark = portfolio["benchmark_return_pct"]

# abs() measures magnitude of deviation regardless of direction
deviations = [
    {
        "ticker":    h["ticker"],
        "return":    h["return_pct"],
        "deviation": abs(h["return_pct"] - benchmark),
        "direction": "outperform" if h["return_pct"] > benchmark else "underperform"
    }
    for h in portfolio["holdings"]
]

# Highest absolute deviation from benchmark
max_dev = max(deviations, key=lambda x: x["deviation"])
print(f"\nLargest deviation from benchmark ({benchmark}%): "
      f"{max_dev['ticker']} at {max_dev['deviation']:.1f}% ({max_dev['direction']})")

for d in sorted(deviations, key=lambda x: x["deviation"], reverse=True):
    print(f"  {d['ticker']}: {d['return']:+.1f}%  |  dev={d['deviation']:.1f}%  [{d['direction']}]")

# --- Example 3: round() for currency precision in invoice JSON ---
raw_invoice = '''
{
    "invoice_id": "INV-2094",
    "currency": "USD",
    "tax_rate": 0.085,
    "items": [
        {"desc": "Consulting",      "qty": 8,  "unit_price": 175.333},
        {"desc": "Cloud Storage",   "qty": 3,  "unit_price": 49.999},
        {"desc": "Support License", "qty": 1,  "unit_price": 299.001}
    ]
}
'''

try:
    invoice = json.loads(raw_invoice)
except json.JSONDecodeError as e:
    raise SystemExit(f"Invoice parse failed: {e.msg}")

# round() to 2dp prevents floating-point artifacts in financial output
line_items = [
    {
        "desc":       item["desc"],
        "qty":        item["qty"],
        "unit_price": round(item["unit_price"], 2),
        "subtotal":   round(item["qty"] * item["unit_price"], 2)
    }
    for item in invoice["items"]
]
subtotal = round(sum(i["subtotal"] for i in line_items), 2)
tax      = round(subtotal * invoice["tax_rate"], 2)
total    = round(subtotal + tax, 2)

print(f"\nInvoice {invoice['invoice_id']}")
for li in line_items:
    print(f"  {li['desc']:<20} {li['qty']} x ${li['unit_price']:.2f} = ${li['subtotal']:.2f}")
print(f"  {'Subtotal':<20} ${subtotal:.2f}")
print(f"  {'Tax (8.5%)':<20} ${tax:.2f}")
print(f"  {'Total':<20} ${total:.2f}")

# --- Example 4: pow() for compound-growth projections ---
raw_growth = '''
{
    "model": "CAGR Projection",
    "base_year": 2024,
    "initial_value": 100000,
    "scenarios": [
        {"label": "Conservative", "cagr": 0.04, "years": 10},
        {"label": "Moderate",     "cagr": 0.08, "years": 10},
        {"label": "Aggressive",   "cagr": 0.15, "years": 10}
    ]
}
'''

try:
    growth = json.loads(raw_growth)
except json.JSONDecodeError as e:
    growth = {"scenarios": [], "initial_value": 0}

print(f"\n{growth['model']} — Base: ${growth['initial_value']:,}")

projections = [
    {
        "label":       s["label"],
        "cagr_pct":    s["cagr"] * 100,
        # pow(base, exp) is equivalent to base**exp but explicit in formulas
        "final_value": round(growth["initial_value"] * pow(1 + s["cagr"], s["years"]), 2),
        "years":       s["years"]
    }
    for s in growth["scenarios"]
]

for p in projections:
    print(f"  {p['label']:<14} {p['cagr_pct']:.0f}% CAGR  →  ${p['final_value']:>12,.2f} after {p['years']}y")

# --- Example 5: Combined pipeline — compute, enrich, and write results ---
results_payload = {
    "run_at":       datetime.now().isoformat(),
    "sensor_stats": {
        "min_temp":  min(temps),
        "max_temp":  max(temps),
        "avg_temp":  round(sum(temps) / len(temps), 2)
    },
    "invoice_total":    total,
    "growth_scenarios": projections,
    "deviation_leaders": sorted(deviations, key=lambda x: x["deviation"], reverse=True)[:3]
}

out_path = os.path.join(OUTPUT_DIR, "builtin_math_results.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results_payload, f, indent=2)
print(f"\nResults written → {out_path}")