# custom_parser.py
# Example: parse simple "key=value" pairs separated by spaces, or CSV-like logs
# Example line: "timestamp=2025-12-05T10:00:00 level=INFO message='Hello' source=app1 temp=72"

import shlex
from typing import Optional, Dict

def parse_line(line: str) -> Optional[Dict]:
    line = line.strip()
    if not line:
        return None

    # Try key=value pairs
    try:
        parts = shlex.split(line)
        data = {}
        for p in parts:
            if '=' in p:
                k, v = p.split('=', 1)
                # remove surrounding quotes
                if v.startswith('"') and v.endswith('"') or v.startswith("'") and v.endswith("'"):
                    v = v[1:-1]
                data[k] = v
        if data:
            # normalize
            return {
                "timestamp": data.get("timestamp"),
                "level": data.get("level"),
                "message": data.get("message") or data.get("msg"),
                "source": data.get("source"),
                **{k: try_number(v) for k, v in data.items() if k not in ("timestamp","level","message","msg","source")}
            }
    except Exception:
        pass

    # fallback: return raw
    return {
        "timestamp": None,
        "level": None,
        "message": line,
        "source": None
    }

def try_number(v: str):
    try:
        if '.' in v:
            return float(v)
        return int(v)
    except Exception:
        return v
