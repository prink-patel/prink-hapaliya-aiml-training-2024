import pika
import time
import random

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

employee__id = 1

while True:

    message = f"sending message id: {employee__id}"

    channel.basic_publish(exchange="", routing_key="letterbox", body=message)

    print(f"send message: {message}")
    time.sleep(random.randint(1, 4))

    employee__id += 1
