# myapp/rabbitmq.py
import os
import pika

def get_rabbitmq_channel():
    """Return a RabbitMQ channel connected to CloudAMQP"""
    url = os.environ.get("RABBITMQ_URL")
    if not url:
        raise ValueError("RABBITMQ_URL environment variable not set")
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    return channel, connection
