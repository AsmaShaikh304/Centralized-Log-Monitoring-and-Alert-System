# syslog_parser.py
# simple syslog line parser (RFC-like but tolerant)
# Example syslog: "Dec  5 10:01:23 myhost appname[123]: INFO - Something happened"

import re
from typing import Optional, Dict
from datetime import datetime

SYSLOG_RE = re.compile(r'^(?P<ts>\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(?P<host>\S+)\s+(?P<rest>.+)$')

LEVEL_RE = re.compile(r'\b(INFO|WARN|WARNING|ERROR|DEBUG|CRITICAL)\b', re.IGNORECASE)

def parse_line(line: str) -> Optional[Dict]:
    line = line.strip()
    if not line:
        return None

    m = SYSLOG_RE.match(line)
    if not m:
        # fallback: try to pull level and message
        level_m = LEVEL_RE.search(line)
        return {
            "timestamp": None,
            "level": level_m.group(1).upper() if level_m else None,
            "message": line,
            "source": None
        }

    ts_text = m.group('ts')
    host = m.group('host')
    rest = m.group('rest')

    # parse level if present
    level_m = LEVEL_RE.search(rest)
    level = level_m.group(1).upper() if level_m else None

    # message: everything after first colon if exists
    msg = rest.split(':', 1)[-1].strip() if ':' in rest else rest

    # convert ts_text (no year) to ISO timestamp — include current year
    try:
        ts_obj = datetime.strptime(ts_text + f' {datetime.now().year}', '%b %d %H:%M:%S %Y')
        timestamp = ts_obj.isoformat()
    except Exception:
        timestamp = None

    return {
        "timestamp": timestamp,
        "level": level,
        "message": msg,
        "source": host
    }
