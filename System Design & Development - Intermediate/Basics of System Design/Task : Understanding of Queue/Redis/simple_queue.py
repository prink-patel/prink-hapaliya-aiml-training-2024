import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Create a queue by using a Redis list
queue_key = 'my_queue'
r.delete(queue_key)  # Ensure the queue is empty

# Add elements to the queue
for i in range(5):
    r.rpush(queue_key, i)

# Get elements from the queue
print(r.lpop(queue_key))  
print(r.brpop(queue_key, timeout=0)) 