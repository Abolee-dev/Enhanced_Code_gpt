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

    target_index = f"{data.get('otel.splunkindex', '').strip()}_logs" if data.get("otel.splunkindex") else SPLUNK_DEFAULT_INDEX

    event = {
        "event": data,
        "index": target_index,
        "sourcetype": "_json"
    }

    try:
        r = session.post(f"{SPLUNK_HEC_URL}/services/collector/event", headers=headers, json=event, timeout=2)
        if r.status_code != 200:
            logging.warning(f"Splunk HEC failed: {r.status_code} - {r.text}")
    except Exception as e:
        logging.error(f"Splunk send error: {e}")
