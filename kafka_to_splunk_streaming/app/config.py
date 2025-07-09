import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
KAFKA_TOPICS = os.getenv("KAFKA_TOPICS", "infra-metrics").split(",")

SPLUNK_HEC_URL = os.getenv("SPLUNK_HEC_URL", "http://splunk-hec:8088")
SPLUNK_TOKEN = os.getenv("SPLUNK_TOKEN", "")
SPLUNK_DEFAULT_INDEX = os.getenv("SPLUNK_INDEX", "main")

KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "splunk-sink-group")
