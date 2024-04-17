import redis

# Create a Redis connection
r = redis.Redis(host="localhost", port=6379, db=0)

# Subscribe to a channel
p = r.pubsub()
p.subscribe("mychannel")

# Receive messages from the channel
while True:
    message = p.parse_response(p.get_message())
    if message:
        print(f'Received message: {message["data"].decode()}')
