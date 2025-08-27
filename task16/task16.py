import asyncio

async def delay(seconds):
    await asyncio.sleep(seconds)

async def run_task():
    print("task starting")
    await asyncio.sleep(2)
    print("task started after 2 seconds")

asyncio.run(run_task())