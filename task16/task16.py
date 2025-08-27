import asyncio

async def my_promise(success):
    if success:
        return "Task completed successfully "
    else:
        raise Exception("Task failed ")

async def main():
    
    try:
        result = await my_promise(True)
        print(result)  
    except Exception as error:
        print(error)
    
     
    try:
        result = await my_promise(False) 
        print(result)  
    except Exception as error:
        print(error)

asyncio.run(main()) 