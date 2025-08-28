import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def task3():
    print("Task 3 started")
    await asyncio.sleep(1)
    raise Exception("Error in Task 3!")

async def main():
    tasks = [task1(), task2(), task3()]
    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        print(f"Caught an exception: {e}")

asyncio.run(main())