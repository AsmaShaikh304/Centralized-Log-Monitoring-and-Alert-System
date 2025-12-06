import requests
import time
import yaml
import logging

with open('config.yaml') as f:
    config = yaml.safe_load(f)

BACKEND_URL = config['backend_url']
INTERVAL = config.get('interval', 5)

logging.basicConfig(level=logging.INFO)

def collect_logs():
    return {
        "level": "INFO",
        "message": "Python agent log",
        "source": "python-agent",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }

def send_log(log):
    try:
        r = requests.post(BACKEND_URL, json=log)
        if r.status_code in (200, 201):
            logging.info("Sent log")
        else:
            logging.error(r.text)
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    while True:
        log = collect_logs()
        send_log(log)
        time.sleep(INTERVAL)
