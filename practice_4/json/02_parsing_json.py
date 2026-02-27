import json

# --- Example 1: Basic loads() with JSONDecodeError trap ---
def safe_parse(raw: str) -> dict | None:
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        # e.lineno and e.colno pinpoint the exact failure location
        print(f"Parse failed at line {e.lineno}, col {e.colno}: {e.msg}")
        return None

valid   = '{"user": "alice", "score": 99}'
invalid = '{"user": "alice", score: 99}'   # missing quotes on key
print(safe_parse(valid))
print(safe_parse(invalid))

# --- Example 2: Parse a deeply nested API response ---
api_response = '''
{
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "roles": ["admin", "editor"],
             "meta": {"last_login": "2024-01-15", "mfa": true}},
            {"id": 2, "name": "Bob",   "roles": ["viewer"],
             "meta": {"last_login": "2023-11-02", "mfa": false}}
        ]
    },
    "pagination": {"page": 1, "total": 2}
}
'''
parsed = json.loads(api_response)

# Extract MFA-enabled admins via nested list comprehension
mfa_admins = [
    u["name"]
    for u in parsed["data"]["users"]
    if u["meta"]["mfa"] and "admin" in u["roles"]
]
print(f"MFA admins: {mfa_admins}")

# --- Example 3: Validate required keys after parsing ---
REQUIRED_KEYS = {"status", "data", "pagination"}

def validate_response(payload: dict, required: set) -> bool:
    missing = required - payload.keys()
    if missing:
        print(f"Schema violation — missing keys: {missing}")
        return False
    return True

validate_response(parsed, REQUIRED_KEYS)

# --- Example 4: Parse JSON with object_hook for auto-transformation ---
def lowercase_keys(d: dict) -> dict:
    # Normalize all keys to lowercase on ingestion
    return {k.lower(): v for k, v in d.items()}

raw = '{"Name": "Charlie", "Score": 87, "Active": true}'
normalized = json.loads(raw, object_hook=lowercase_keys)
print(normalized)  # {'name': 'Charlie', 'score': 87, 'active': True}

# --- Example 5: Parse a JSON array at the root level ---
raw_array = '[{"id": 1, "val": 10}, {"id": 2, "val": 20}, {"id": 3, "val": 5}]'
records = json.loads(raw_array)

# Filter and reshape in one comprehension
high_val = [{"id": r["id"], "val_doubled": r["val"] * 2} for r in records if r["val"] >= 10]
print(high_val)

# --- Example 6: Detect and recover from truncated JSON ---
truncated = '{"key": "value", "nested": {"a": 1'
result = safe_parse(truncated)
if result is None:
    print("Falling back to empty default payload.")
    result = {}
print(result)