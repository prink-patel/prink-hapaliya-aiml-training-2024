# Write program to share a single variable between two continuous loops.
# Create one variable, using one loop increase that one variable by +5, using second loop decrease that same variable by -2

from threading import Thread, Lock
from time import sleep

var=0
def increase(lock):
    global var
    while True:
        lock.acquire()
        var= var+5
        print(var)
        lock.release()
        sleep(0.1)

def decrease(lock):
    global var
    while True:
        lock.acquire()        
        var=var-2
        print(var)
        lock.release()
        sleep(0.1)

lock = Lock()
t1 = Thread(target=increase, args=(lock,))
t2 = Thread(target=decrease, args=(lock))

t1.start()
t2.start()

t1.join()
t2.join()

