import json
from datetime import datetime, date

# --- Example 1: dumps() with indent and sort_keys ---
config = {
    "zebra_key": True,
    "alpha_key": [3, 1, 2],
    "meta": {"created": "2024-01-01", "owner": "system"}
}

# sort_keys ensures deterministic output — critical for diffs and hashing
pretty = json.dumps(config, indent=4, sort_keys=True)
print(pretty)

# --- Example 2: Compact output with custom separators ---
# (',', ':') strips all whitespace — ideal for network transmission
compact = json.dumps(config, separators=(',', ':'), sort_keys=True)
print(f"Compact ({len(compact)} bytes): {compact}")

# --- Example 3: Custom serializer for datetime objects ---
class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            # ISO-8601 is the JSON-safe standard for datetimes
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, set):
            # Sets are not JSON-serializable; convert to sorted list for stability
            return sorted(list(obj))
        return super().default(obj)

event = {
    "name": "Deploy v2.0",
    "timestamp": datetime(2024, 6, 15, 14, 30, 0),
    "release_date": date(2024, 6, 15),
    "tags": {"backend", "critical", "automated"},
    "meta": {
        "triggered_by": "CI",
        "duration_ms": 4823
    }
}

serialized = json.dumps(event, cls=ExtendedEncoder, indent=2)
print(serialized)

# --- Example 4: ensure_ascii=False for unicode preservation ---
multilingual = {
    "greeting_ja": "こんにちは",
    "greeting_ar": "مرحبا",
    "greeting_ru": "Привет"
}
# ensure_ascii=False keeps unicode characters readable in the output file
unicode_out = json.dumps(multilingual, ensure_ascii=False, indent=2)
print(unicode_out)

# --- Example 5: Round-trip integrity check ---
original = {"ids": [1, 2, 3], "active": True, "ratio": 0.75}
serialized_str = json.dumps(original, sort_keys=True)
restored = json.loads(serialized_str)
assert original == restored, "Round-trip integrity failed"
print("Round-trip integrity: PASSED")

# --- Example 6: Serialize a list of dataclass-style dicts with filtering ---
records = [
    {"user": "alice", "score": 91, "verified": True,  "joined": date(2022, 3, 10)},
    {"user": "bob",   "score": 45, "verified": False, "joined": date(2023, 7, 22)},
    {"user": "carol", "score": 78, "verified": True,  "joined": date(2021, 11, 5)},
]
# Serialize only verified users, sorted by score descending
filtered = sorted(
    [r for r in records if r["verified"]],
    key=lambda x: x["score"],
    reverse=True
)
output = json.dumps(filtered, cls=ExtendedEncoder, indent=2)
print(output)