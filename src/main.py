from fastapi import FastAPI
from src.controller import items, auth

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(auth.router)
app.include_router(items.router)
