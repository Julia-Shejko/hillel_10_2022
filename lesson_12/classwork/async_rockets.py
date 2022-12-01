import asyncio
import random
from typing import Coroutine


def random_delay():
    return random.random() * 3


def random_countdown():
    return random.randint(1, 5)


async def launch_rocket(num: int, delay: float, countdown: int) -> None:
    await asyncio.sleep(delay)
    for i in reversed(range(1, countdown + 1)):
        print(f"{num}:{i}...")
        await asyncio.sleep(1)
    print(f"🚀 Rocket {num} is launched")


# async def run():
# threads: list[Thread] = [
#     Thread(target=launch_rocket, args=[i, random_delay(), random_countdown()])
#     for i in range(1, 1_000_000)
# ]


async def main():
    tasks: list[Coroutine] = [
        launch_rocket(num=i, delay=random_delay(), countdown=random_countdown()) for i in range(100_000)
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
