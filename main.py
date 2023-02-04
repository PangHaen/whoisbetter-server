from fastapi import FastAPI

from app.user import controller as user_controller

app = FastAPI()

app.include_router(user_controller.router)
