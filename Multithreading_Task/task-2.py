# Write program to share a single variable between two continuous loops.
# Create one variable, using one loop increase that one variable by +5, using second loop decrease that same variable by -2

from threading import Thread, Lock
from time import sleep

var=0
def increase(lock,num):
    global var
    for i in range(num):
        lock.acquire()
        var= var+5
        print(var)
        lock.release()
        sleep(0.1)

def decrease(lock,num):
    global var
    for i in range(num):
        lock.acquire()        
        var=var-2
        print(var)
        lock.release()
        sleep(0.1)

lock = Lock()
t1 = Thread(target=increase, args=(lock,5))
t2 = Thread(target=decrease, args=(lock,5))

t1.start()
t2.start()

t1.join()
t2.join()

