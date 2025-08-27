import asyncio

async def start_with_delay(num):
    
    await asyncio.sleep(1)
    return num

async def multiply_by_two(num):
    
    return num * 2

async def add_five(num):
    
    return num + 5

async def main():
    
    start_value = await start_with_delay(10)
    multiplied = await multiply_by_two(start_value)
    result = await add_five(multiplied)
    print(result)  

asyncio.run(main())