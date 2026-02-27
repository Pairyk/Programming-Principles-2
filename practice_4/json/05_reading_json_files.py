import json
import os

OUTPUT_DIR = "practice_4/json/output"

# --- Example 1: Read with context manager and FileNotFoundError trap ---
config_path = os.path.join(OUTPUT_DIR, "pipeline_config.json")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    print(f"Pipeline: {config['pipeline']} v{config['version']}")
except FileNotFoundError:
    print(f"Config not found at {config_path} — using defaults.")
    config = {}
except json.JSONDecodeError as e:
    print(f"Corrupt JSON at line {e.lineno}: {e.msg}")
    config = {}

# --- Example 2: Schema-style key validation after loading ---
REQUIRED_CONFIG_KEYS = {"pipeline", "version", "steps", "alerts"}

def validate_schema(data: dict, required: set, label: str = "payload") -> bool:
    missing = required - data.keys()
    if missing:
        print(f"[{label}] Missing required keys: {missing}")
        return False
    print(f"[{label}] Schema OK")
    return True

validate_schema(config, REQUIRED_CONFIG_KEYS, label="pipeline_config")

# --- Example 3: Load and query a JSON log file ---
log_path = os.path.join(OUTPUT_DIR, "run_log.json")

try:
    with open(log_path, "r", encoding="utf-8") as f:
        run_log = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    run_log = []

failed_runs = [r for r in run_log if r.get("status") == "failed"]
print(f"Failed runs: {len(failed_runs)} of {len(run_log)}")

# --- Example 4: Load and merge multiple dept files ---
merged_users = []
for fname in os.listdir(OUTPUT_DIR):
    if fname.startswith("dept_") and fname.endswith(".json"):
        fpath = os.path.join(OUTPUT_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                dept_data = json.load(f)
            # Validate expected structure before accessing nested keys
            if "members" not in dept_data:
                print(f"Skipping {fname}: missing 'members' key")
                continue
            merged_users.extend(dept_data["members"])
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error reading {fname}: {e}")

print(f"Total merged users: {len(merged_users)}")
# Sort merged list by id
merged_users.sort(key=lambda u: u["id"])
for u in merged_users:
    print(f"  {u['id']}: {u['name']} ({u['dept']})")

# --- Example 5: Load with object_hook to auto-parse nested types ---
import re
from datetime import datetime

def parse_iso_dates(d: dict) -> dict:
    # Detect ISO datetime strings and convert them to datetime objects on load
    iso_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
    return {
        k: datetime.fromisoformat(v) if isinstance(v, str) and iso_pattern.match(v) else v
        for k, v in d.items()
    }

try:
    with open(log_path, "r", encoding="utf-8") as f:
        typed_log = json.load(f, object_hook=parse_iso_dates)
    for entry in typed_log:
        ts = entry.get("ts")
        if isinstance(ts, datetime):
            print(f"  Run {entry['run_id']}: {ts.strftime('%Y-%m-%d %H:%M')}")
except (FileNotFoundError, json.JSONDecodeError):
    print("Log unavailable for typed load.")

# --- Example 6: Safe deep-read utility with dotted key path ---
def deep_get(data: dict, path: str, default=None):
    # Access nested keys via "a.b.c" notation without chained .get() calls
    keys = path.split(".")
    for key in keys:
        if not isinstance(data, dict):
            return default
        data = data.get(key, default)
    return data

if config:
    source = deep_get(config, "steps.0.source", default="unknown")
    alert_emails = deep_get(config, "alerts.on_failure", default=[])
    print(f"Extract source: {source}")
    print(f"Alert recipients: {alert_emails}")