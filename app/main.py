from fastapi import FastAPI
from app.endpoints import chat

app = FastAPI()

# Include router from endpoints
app.include_router(chat.router)

