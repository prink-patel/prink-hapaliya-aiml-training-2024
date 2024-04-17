from kafka import KafkaProducer
import json

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Add data to the Kafka queue
data = {'message': 'Hello, Kafka!'}
producer.send('my_topic', json.dumps(data).encode('utf-8'))

# Close the Kafka producer
producer.close()