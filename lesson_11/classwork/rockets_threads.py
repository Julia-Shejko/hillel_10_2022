import random
import time
from threading import Thread


def random_delay():
    return random.random() * 3


def random_countdown():
    return random.randint(1, 5)


def launch_rocket(num: int, delay: float, countdown: int) -> None:
    time.sleep(delay)
    for i in reversed(range(1, countdown + 1)):
        print(f"{num}:{i}...")
        time.sleep(1)
    print(f"🚀 Rocket {num} is launched")


def run_sync():
    for i in range(1, 11):
        launch_rocket(i, random_delay(), random_countdown())


def run_threads():
    threads: list[Thread] = [
        Thread(target=launch_rocket, args=[i, random_delay(), random_countdown()]) for i in range(1, 1_000_000)
    ]

    for thread in threads:
        thread.start()


def main():
    # run_sync()
    run_threads()


if __name__ == "__main__":
    main()
