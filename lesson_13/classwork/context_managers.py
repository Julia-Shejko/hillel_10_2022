import asyncio
from typing import Any

# def logger(func):
#     def inner(*args, **kwargs):
#         print(f"Executing {func.__name__}")
#         return func(*args, **kwargs)
#     return inner


class Cache:
    def __init__(self) -> None:
        self._storage: dict = {}

    def open_connection(self):
        print("Connection opened")

    def close_connection(self):
        print("Close connection")

    async def save(self, key, value) -> None:
        await asyncio.sleep(0)
        print(f"Saving {key} to the cache")
        self._storage[key] = value

    async def __aenter__(self):
        print("Opening connection")
        await asyncio.sleep(0)
        return self

    async def __aexit__(self, *args, **kwargs):
        print("Closing connection")

    async def get(self, key) -> Any:
        await asyncio.sleep(0)
        return self._storage[key]

    def __str__(self):
        return f"Cache: {self._storage}"


async def main():
    cache = Cache()

    name = "John"
    age = 30
    async with cache:
        await cache.save(key=name, value=age)

    name = "Marry"
    age = 50
    async with cache:
        await cache.save(key=name, value=age)

    print(cache)


asyncio.run(main())
