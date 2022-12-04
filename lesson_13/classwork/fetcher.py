import asyncio

import requests

# from threading import Thread

URL = "http://localhost:8000/"


def callback(url):
    response = requests.get(url)
    print(response)


# threads = [Thread(target=callback, args=[""]) for i in range(5)]

# for thread in threads:
#     thread.start()


async def main():
    tasks = [asyncio.to_thread(callback, URL) for _ in range(5)]
    await asyncio.gather(*tasks)


asyncio.run(main())

# responses = []

# for thread in threads:
#     thread.join()

# for _ in range(5):
#     response = requests.get("http://localhost:8000/")
#     responses.append(response)

# values = [response.json()["random value"] for response in responses]

# print(values)
