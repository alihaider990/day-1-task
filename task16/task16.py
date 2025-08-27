import asyncio
import aiohttp

async def get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                print("User:", data)
    except Exception as error:
        print("Error:", error)

asyncio.run(get_user())