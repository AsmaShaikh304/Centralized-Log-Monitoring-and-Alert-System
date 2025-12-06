# alert_pipeline.py
# Simple alerting pipeline that fetches logs from backend and evaluates rules from backend /alertRules
# WARNING: uses a tiny safe-eval pattern for numeric comparisons and simple expressions.

import requests
import time

BACKEND_BASE = "http://localhost:8080"
ALERTRULES_ENDPOINT = f"{BACKEND_BASE}/alertRules"
LOGS_ENDPOINT = f"{BACKEND_BASE}/logs"

POLL_INTERVAL = 10  # seconds

def fetch_alert_rules():
    try:
        r = requests.get(ALERTRULES_ENDPOINT, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("[ALERT] failed to fetch rules:", e)
        return []

def fetch_recent_logs():
    try:
        r = requests.get(LOGS_ENDPOINT, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("[ALERT] failed to fetch logs:", e)
        return []

def eval_simple_condition(cond: str, log: dict) -> bool:
    """
    Evaluate simple conditions like:
      "temp > 50"
      "level == 'ERROR'"
      "message.find('timeout') != -1"
    This function provides a tiny sandbox: only log values allowed via `vars`.
    """
    if not cond:
        return False
    # prepare safe namespace with log fields
    safe_locals = {}
    for k, v in log.items():
        # provide numeric values and strings, avoid nested complex objects
        if isinstance(v, (int, float, str)):
            safe_locals[k] = v
    try:
        # no builtins allowed
        return bool(eval(cond, {"__builtins__": {}}, safe_locals))
    except Exception:
        return False

def run_once():
    rules = fetch_alert_rules()
    logs = fetch_recent_logs()

    for rule in rules:
        cond = rule.get("condition")
        name = rule.get("name")
        for log in logs:
            if eval_simple_condition(cond, log):
                # simple action: print + notify backend /alerts (if exists)
                print(f"[ALERT] rule matched: {name} -> log id {log.get('id')}")
                try:
                    payload = {
                        "rule_name": name,
                        "message": log.get("message"),
                        "timestamp": log.get("timestamp") or log.get("ingestion_time")
                    }
                    r = requests.post(f"{BACKEND_BASE}/alerts", json=payload, timeout=5)
                    if r.status_code in (200,201):
                        print("[ALERT] alert saved in backend")
                    else:
                        print("[ALERT] failed saving alert:", r.status_code, r.text)
                except Exception as e:
                    print("[ALERT] failed to post alert:", e)

if __name__ == "__main__":
    # run once for manual invocation
    run_once()
