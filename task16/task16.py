import asyncio

async def my_promise(success):
    if success:
        return True
    else:
        raise Exception("error message")

async def main():
    try:
        result = await my_promise(True)
        print(result)  
    except Exception as error:
        print(error)

asyncio.run(main())


async def my_promise(success):
    if success:
        return True
    else:
        raise Exception("error message")

async def main():
    try:
        result = await my_promise(false)
        print(result)  
    except Exception as error:
        print(error)

asyncio.run(main())






