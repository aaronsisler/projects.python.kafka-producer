from kafka import KafkaProducer
from config import kafka_host, kafka_topic


class KafkaProducerService:
    _producer: KafkaProducer

    def __init__(self):
        self._producer = KafkaProducer(bootstrap_servers=kafka_host)

    def publish_message(self, message):
        self._producer.send(kafka_topic, message)
