import threading
from queue import Queue
from time import sleep


def foo(value: str, queue: Queue):
    print("I am inside")
    sleep(5)
    queue.put(value)
    print("Going out")


q = Queue()
thread = threading.Thread(target=foo, args=("Hello world", q), daemon=True)
thread.start()
result = q.get()
print(f"{result=}")
