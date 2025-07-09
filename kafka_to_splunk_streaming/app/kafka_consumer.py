from confluent_kafka import Consumer
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPICS, KAFKA_GROUP_ID

def create_consumer():
    consumer = Consumer({
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': KAFKA_GROUP_ID,
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(KAFKA_TOPICS)
    return consumer
