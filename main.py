import os
import aiohttp
from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()

load_dotenv(verbose=True)


@app.get("/")
async def root():
    fifa_token = os.getenv('FIFA_API_KEY')

    session_timeout = aiohttp.ClientTimeout(total=None, sock_read=60, sock_connect=60)
    async with aiohttp.ClientSession(timeout= session_timeout, headers={'Authorization' : fifa_token}) as client:
        async with client.get(url=f'https://api.nexon.co.kr/fifaonline4/v1.0/users?nickname=내이름은무리뉴') as response:
            res = await response.json()
            print(res['accessId'])
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
