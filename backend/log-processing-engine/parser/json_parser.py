# json_parser.py
# parse lines that are plain JSON objects

import json
from typing import Optional, Dict

def parse_line(line: str) -> Optional[Dict]:
    line = line.strip()
    if not line:
        return None
    try:
        obj = json.loads(line)
        # normalize keys to expected fields
        return {
            "timestamp": obj.get("timestamp") or obj.get("time") or None,
            "level": obj.get("level"),
            "message": obj.get("message"),
            "source": obj.get("source"),
            **{k: v for k, v in obj.items() if k not in ("timestamp","time","level","message","source")}
        }
    except json.JSONDecodeError:
        return None
