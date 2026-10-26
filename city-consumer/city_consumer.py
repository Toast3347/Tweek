
import json
import os

import pika

from models.message import Message


def process_message(ch, method, properties, body):
    try:
        data = json.loads(body.decode("utf-8"))

        if not isinstance(data, dict):
            raise ValueError("Message must be a JSON object")

        author = data.get("author")
        message_body = data.get("body")

        if not isinstance(author, str) or not author.strip():
            raise ValueError("author must be a non-empty string")

        if not isinstance(message_body, str) or not message_body.strip():
            raise ValueError("body must be a non-empty string")

        message = Message(
            author=author,
            body=message_body,
        )

        print(f"{message.author}: {message.body}", flush=True)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as error:
        print(f"Invalid message: {error}", flush=True)

        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=False,
        )


def main():
    rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host)
    )

    channel = connection.channel()

    channel.queue_declare(
        queue="tweek_messages",
        durable=True,
    )

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue="tweek_messages",
        on_message_callback=process_message,
        auto_ack=False,
    )

    print("Herro, this is City consumer. How can I take your message?", flush=True)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Stopping consumer...", flush=True)
        channel.stop_consuming()
    finally:
        if connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
