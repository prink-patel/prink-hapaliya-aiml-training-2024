import redis

# Create a Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

# Publish messages to a channel
for i in range(10):
    r.publish('mychannel', f'Message {i}')