import requests
import json
import logging
from app.config import SPLUNK_HEC_URL, SPLUNK_TOKEN, SPLUNK_DEFAULT_INDEX

logging.basicConfig(level=logging.INFO)

session = requests.Session()
headers = {
    'Authorization': f'Splunk {SPLUNK_TOKEN}',
    'Content-Type': 'application/json'
}

def send_to_splunk(payload_raw):
    try:
        data = json.loads(payload_raw)
    except json.JSONDecodeError:
        logging.warning("Invalid JSON")
        return

    # 🔧 Append custom_text to otel.splunkindex
    base_index = data.get("otel.splunkindex", "").strip()
    if base_index:
        full_index = f"{base_index}_{CUSTOM_TEXT}"
    else:
        full_index = SPLUNK_DEFAULT_INDEX

    # Optional: update the message payload with the full index
    data["otel.splunkindex"] = full_index

    event = {
        "event": data,
        "index": full_index,
        "sourcetype": "_json"
    }

    try:
        r = session.post(f"{SPLUNK_HEC_URL}/services/collector/event", headers=headers, json=event, timeout=2)
        if r.status_code != 200:
            logging.warning(f"Splunk HEC failed: {r.status_code} - {r.text}")
    except Exception as e:
        logging.error(f"Splunk send error: {e}")
