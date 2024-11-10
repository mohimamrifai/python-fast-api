from fastapi import APIRouter
from src.utils.jsonCustomResponse import jsonCustomResponse
from src.models.authModel import Login, Register

router = APIRouter()

@router.post("/login")
async def login(login: Login):
    # TODO: Implement login logic
    # TODO: Check if user exists
    # TODO: Check if password is correct
    # TODO: Generate JWT token
    return jsonCustomResponse(200, "Logged in successfully", {"token": "1234567890"})

@router.post("/register")
async def register(register: Register):
    # TODO: Implement register logic
    # TODO: Check if user exists
    # TODO: Check if password is correct
    # TODO: Generate JWT token
    return jsonCustomResponse(200, "Registered successfully", {"token": "1234567890"})
