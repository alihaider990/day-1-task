import asyncio

async def sleep_ms(milliseconds):
    
    seconds = milliseconds / 1000
    await asyncio.sleep(seconds)

async def test_sleep():
    print("starting the task")
    await sleep_ms(1500)  
    print("Finished after 1.5 seconds")

asyncio.run(test_sleep())