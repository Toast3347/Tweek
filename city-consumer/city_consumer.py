import pika
import json
from models.message import Message

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue="tweek_messages", durable=True)

# Process
def process_message(ch, method, properties, body):
    data = json.loads(body.decode("utf-8"))

    message = Message(author=data["author"], body=data["body"])
    print(f"{message.author}: {message.body}")

    # Acknowledge successful processing
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue="tweek_messages",
    on_message_callback=process_message,
    auto_ack=False
)

print("Herro, this is City consumer. How can I take your message?")
channel.start_consuming()
