from flask import Flask, request

from services.kafka_producer_service import KafkaProducerService

app = Flask(__name__)


@app.route('/send-message', methods=['POST'])
def send_message():
    request_data = request.get_json()
    if "message" not in request_data:
        return {"status": 400, "body": "Bad request"}

    print(request.get_json())
    message = request_data["message"]
    encoded_message = str.encode(message)
    print("Up Here")
    kafka_producer_service = KafkaProducerService()
    print("Mid Here")
    kafka_producer_service.publish_message(encoded_message)
    print("Down Here")
    return 'Hello, World!'
