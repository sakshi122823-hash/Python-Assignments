import threading

count = 0

lock = threading.Lock()

def increment():
    global count
    for i in range(10):
        lock.acquire()
        count = count + 1
        lock.release()

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final value:", count)
