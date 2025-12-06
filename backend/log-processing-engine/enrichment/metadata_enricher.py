# metadata_enricher.py
# Add ingestion metadata and simple enrichment (geo/host tags placeholder)

import socket
from datetime import datetime
from typing import Dict

def enrich(log: Dict) -> Dict:
    """
    Enrich a log dict with:
     - ingestion_time (ISO)
     - host (local hostname if missing)
     - short_message (trimmed)
    """
    enriched = dict(log)  # shallow copy

    # ingestion timestamp
    enriched.setdefault("ingestion_time", datetime.utcnow().isoformat() + "Z")

    # host/source fallback
    if not enriched.get("source"):
        try:
            enriched["source"] = socket.gethostname()
        except Exception:
            enriched["source"] = "unknown"

    # ensure message exists and add short_message
    msg = enriched.get("message") or ""
    enriched["short_message"] = (msg[:200] + '...') if len(msg) > 200 else msg

    # try to normalize level
    level = enriched.get("level")
    if level:
        enriched["level"] = str(level).upper()

    return enriched
