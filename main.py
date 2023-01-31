import os
import aiohttp
from fastapi import FastAPI

from app.router.user import controller as user_controller

app = FastAPI()

app.include_router(user_controller.router)
