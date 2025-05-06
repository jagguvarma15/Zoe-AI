import json
from pathlib import Path
from datetime import datetime

LOG_PATH = Path("logs/eval_log.jsonl")
LOG_PATH.parent.mkdir(exist_ok=True)

def log_evaluation(data: dict):
    data["timestamp"] = datetime.utcnow().isoformat()
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(data) + "\n")
