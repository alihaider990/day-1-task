import asyncio
import aiohttp

async def get_posts():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://jsonplaceholder.typicode.com/posts") as response:
                data = await response.json()
                print("First 5 post titles:")
                for post in data[:5]:
                    print(post["title"])
    except Exception as e:
        print("Error fetching posts:", e)

async def get_single_post():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://jsonplaceholder.typicode.com/posts/1") as response:
                data = await response.json()
                print("\nSingle post (/posts/1):")
                print(data)
    except Exception as e:
        print("Error fetching single post:", e)

async def wrong_url():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://jsonplaceholder.typicode.com/wrongurl") as response:
                data = await response.text()
                print("\nWrong URL response:")
                print(data)
    except Exception as e:
        print("\nError with wrong URL:", e)

async def get_user_posts(user_id):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
            async with session.get(url) as response:
                data = await response.json()
                print(f"\nPosts of user {user_id}:")
                for post in data:
                    print(post["title"])
    except Exception as e:
        print(f"Error fetching posts for user {user_id}:", e)

async def main():
    await get_posts()
    await get_single_post()
    await wrong_url()
    await get_user_posts(1)


if __name__ == "__main__":
    asyncio.run(main())