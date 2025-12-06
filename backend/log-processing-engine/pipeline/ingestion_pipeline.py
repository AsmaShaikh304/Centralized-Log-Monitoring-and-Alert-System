# ingestion_pipeline.py
# Read log files from ./input_logs/ (relative to this file), parse, enrich, and POST to backend /logs

import os
import time
import requests
from pathlib import Path

from ..parser.json_parser import parse_line as parse_json
from ..parser.syslog_parser import parse_line as parse_syslog
from ..parser.custom_parser import parse_line as parse_custom
from ..enrichment.metadata_enricher import enrich

# CONFIG — change if needed
INPUT_DIR = Path(__file__).resolve().parents[1] / "input_logs"  # clmas/log-processing-engine/input_logs
BACKEND_LOG_ENDPOINT = "http://localhost:8080/logs"  # your backend endpoint for logs
SLEEP_BETWEEN_FILES = 0.2

def detect_and_parse(line: str):
    # Prefer JSON
    obj = parse_json(line)
    if obj:
        return obj
    obj = parse_syslog(line)
    if obj and (obj.get("message") or obj.get("level")):
        return obj
    return parse_custom(line)

def post_to_backend(log_obj: dict):
    try:
        # post JSON to backend
        resp = requests.post(BACKEND_LOG_ENDPOINT, json=log_obj, timeout=5)
        resp.raise_for_status()
        return True, resp.json() if resp.content else {}
    except Exception as e:
        return False, str(e)

def process_file(path: Path):
    print(f"[INGEST] processing {path}")
    with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
        for line in fh:
            parsed = detect_and_parse(line)
            if not parsed:
                continue
            enriched = enrich(parsed)
            ok, resp = post_to_backend(enriched)
            if ok:
                print("[INGEST] posted:", resp)
            else:
                print("[INGEST] failed to post:", resp)
            time.sleep(SLEEP_BETWEEN_FILES)

def run_once():
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted([p for p in INPUT_DIR.iterdir() if p.is_file()])
    if not files:
        print("[INGEST] no files in", INPUT_DIR)
        return
    for p in files:
        process_file(p)

if __name__ == "__main__":
    # simple runner: process once
    run_once()
