from kafka import KafkaConsumer
import json

# Create a Kafka consumer
consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092', group_id='my_group')

# Get data from the Kafka queue
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")

# Close the Kafka consumer
consumer.close()