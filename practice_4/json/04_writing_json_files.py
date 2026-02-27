import json
import os
from datetime import datetime

OUTPUT_DIR = "practice_4/json/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Example 1: Write a nested dict with utf-8 encoding and context manager ---
pipeline_config = {
    "pipeline": "etl_nightly",
    "version": 2,
    "schedule": "0 2 * * *",
    "steps": [
        {"name": "extract",   "source": "postgres", "timeout": 120},
        {"name": "transform", "rules": ["dedupe", "normalize", "cast_types"]},
        {"name": "load",      "target": "bigquery",  "mode": "append"}
    ],
    "alerts": {
        "on_failure": ["ops@company.com"],
        "on_success": []
    }
}

config_path = os.path.join(OUTPUT_DIR, "pipeline_config.json")
# utf-8 encoding prevents mojibake on Windows systems
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(pipeline_config, f, indent=4, sort_keys=True)
print(f"Written: {config_path}")

# --- Example 2: Append a new run record to a JSON log file ---
log_path = os.path.join(OUTPUT_DIR, "run_log.json")

def append_run_log(path: str, entry: dict) -> None:
    # Load existing log or start fresh — handles missing file gracefully
    try:
        with open(path, "r", encoding="utf-8") as f:
            log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        log = []

    log.append(entry)

    with open(path, "w", encoding="utf-8") as f:
        # ensure_ascii=False preserves any unicode in log messages
        json.dump(log, f, indent=2, ensure_ascii=False)

append_run_log(log_path, {"run_id": 1, "status": "success", "ts": datetime.now().isoformat()})
append_run_log(log_path, {"run_id": 2, "status": "failed",  "ts": datetime.now().isoformat()})
print(f"Log updated: {log_path}")

# --- Example 3: Write multiple files from a dataset split by category ---
users = [
    {"id": 1, "name": "Alice", "dept": "engineering"},
    {"id": 2, "name": "Bob",   "dept": "marketing"},
    {"id": 3, "name": "Carol", "dept": "engineering"},
    {"id": 4, "name": "Dave",  "dept": "marketing"},
]

# Group users by department
from collections import defaultdict
dept_map = defaultdict(list)
for user in users:
    dept_map[user["dept"]].append(user)

for dept, members in dept_map.items():
    path = os.path.join(OUTPUT_DIR, f"dept_{dept}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"department": dept, "members": members}, f, indent=2)
    print(f"Written: {path}")

# --- Example 4: Atomic write using a temp file to prevent corruption ---
import tempfile
import shutil

def atomic_write_json(path: str, data: dict) -> None:
    dir_name = os.path.dirname(path)
    # Write to a temp file first; only replace target on success
    with tempfile.NamedTemporaryFile("w", dir=dir_name, delete=False,
                                     suffix=".tmp", encoding="utf-8") as tmp:
        json.dump(data, tmp, indent=4)
        tmp_path = tmp.name
    shutil.move(tmp_path, path)  # atomic on most OS/filesystems

atomic_path = os.path.join(OUTPUT_DIR, "atomic_config.json")
atomic_write_json(atomic_path, {"safe_write": True, "version": 1})
print(f"Atomic write complete: {atomic_path}")

# --- Example 5: Write with custom encoder for non-standard types ---
class SafeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return sorted(list(obj))
        return super().default(obj)

report = {
    "generated_at": datetime.now(),
    "unique_tags": {"python", "json", "etl"},
    "metrics": {"rows_processed": 15000, "errors": 3}
}
report_path = os.path.join(OUTPUT_DIR, "report.json")
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, cls=SafeEncoder, indent=2)
print(f"Report written: {report_path}")