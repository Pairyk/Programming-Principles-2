import json

# JSON supports: strings, numbers, booleans, null, arrays, objects
# Python equivalents: str, int/float, bool, None, list, dict

raw_json = '''
{
    "project": "DataPipeline",
    "version": 3,
    "stable": true,
    "deprecated": false,
    "checksum": null,
    "config": {
        "max_retries": 5,
        "timeout": 30.5,
        "allowed_methods": ["GET", "POST", "PUT"],
        "auth": {
            "type": "oauth2",
            "scopes": ["read", "write", "admin"],
            "tokens": {
                "access": "abc123",
                "refresh": "xyz789",
                "expiry": 3600
            }
        }
    },
    "environments": [
        {"name": "dev",  "url": "http://dev.local",  "active": true},
        {"name": "prod", "url": "https://prod.io",   "active": false}
    ]
}
'''

# --- Example 1: Parse and verify Python type mappings ---
data = json.loads(raw_json)
print(type(data["stable"]))       # <class 'bool'>
print(type(data["checksum"]))     # <class 'NoneType'>
print(type(data["version"]))      # <class 'int'>
print(type(data["config"]["timeout"]))  # <class 'float'>

# --- Example 2: Deep-access nested keys safely ---
# .get() prevents KeyError on optional fields
token_expiry = data.get("config", {}).get("auth", {}).get("tokens", {}).get("expiry", 0)
print(f"Token expiry: {token_expiry}s")

# --- Example 3: Traverse nested list of objects ---
active_envs = [env["name"] for env in data["environments"] if env["active"]]
print(f"Active environments: {active_envs}")

# --- Example 4: Null and boolean handling in conditional logic ---
if data["checksum"] is None:
    print("Checksum not yet computed — pipeline will recalculate.")

if not data["config"]["auth"]["tokens"].get("revoked", False):
    print("Token is currently valid.")

# --- Example 5: Reconstruct nested structure programmatically ---
scopes = data["config"]["auth"]["scopes"]
scope_map = {scope: idx for idx, scope in enumerate(scopes)}
print(f"Scope index map: {scope_map}")

# --- Example 6: Validate expected JSON type contract ---
EXPECTED_TYPES = {
    "project": str,
    "version": int,
    "stable": bool,
}
for key, expected in EXPECTED_TYPES.items():
    actual = type(data.get(key))
    status = "OK" if actual == expected else f"MISMATCH (got {actual})"
    print(f"  {key}: {status}")