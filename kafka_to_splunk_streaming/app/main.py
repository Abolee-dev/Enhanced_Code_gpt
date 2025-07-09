from app.kafka_consumer import create_consumer
from app.splunk_sender import send_to_splunk
import logging

def run():
    consumer = create_consumer()
    logging.info("Kafka → Splunk connector started")

    try:
        while True:
            msg = consumer.poll(timeout=0.1)
            if msg is None:
                continue
            if msg.error():
                logging.error(f"Kafka error: {msg.error()}")
                continue

            try:
                payload = msg.value().decode("utf-8")
                send_to_splunk(payload)
            except Exception as e:
                logging.error(f"Processing error: {e}")
    except KeyboardInterrupt:
        logging.info("Graceful shutdown")
    finally:
        consumer.close()

if __name__ == "__main__":
    run()
