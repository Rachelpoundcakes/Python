import threading
import time

def thread_1():
    while True:
        print('쓰레드1 동작')
        time.sleep(1.0)

thr = threading.Thread(target=thread_1)
thr.start()

while True:  # infinite loop
    print("메인동작")
    time.sleep(2.0)

"""
쓰레드1 동작
쓰레드1 동작
메인동작
쓰레드1 동작
쓰레드1 동작
메인동작

"""