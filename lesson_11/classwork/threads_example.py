from threading import Thread
from time import perf_counter, sleep


def foo(message: str, delay: int):
    for _ in range(5):
        sleep(delay)
        print(message)


thread_1 = Thread(target=foo, args=["I still working", 1])
thread_2 = Thread(target=foo, args=["Another message", 1])

start_time = perf_counter()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

end_time = perf_counter()
print(end_time - start_time)
