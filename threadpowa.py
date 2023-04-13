import threading
user = "Eheh"
mutex = threading.Lock()
import time

def fonction1():
    global user
    while True:
        mutex.acquire()
        user = "Bouh"
        print(user)
        mutex.release()
        time.sleep(1)

def fonction2():
    global user
    while True:
        mutex.acquire()
        user = "Ahah"
        print(user)
        mutex.release()
        time.sleep(1)


thread1 = threading.Thread(target=fonction1)
thread2 = threading.Thread(target=fonction2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()