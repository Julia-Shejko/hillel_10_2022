import asyncio


async def client_1():
    print("I want burger")
    print("I want coffee")
    await asyncio.sleep(5)
    print("Done")


async def client_2():
    print("I want Big tasty")
    await asyncio.sleep(3)
    print("Done")


async def main():
    await asyncio.gather(client_1(), client_2())
    # await client_1()
    # await client_2()


if __name__ == "__main__":
    asyncio.run(main())
