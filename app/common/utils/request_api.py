import os
import aiohttp
from dotenv import load_dotenv

load_dotenv(verbose=True)

API_URL = 'https://api.nexon.co.kr/fifaonline4/v1.0'
FIFA_TOKEN = os.getenv('FIFA_API_KEY')


async def request_api(url, params):
    session_timeout = aiohttp.ClientTimeout(total=None, sock_read=60, sock_connect=60)
    async with aiohttp.ClientSession(timeout=session_timeout, headers={'Authorization': FIFA_TOKEN}) as client:
        async with client.get(url=f'{API_URL}{url}', params=params) as response:
            res = await response.json()
            return res



