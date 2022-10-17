from typing import List
from fastapi import APIRouter, Depends, HTTPException
from ..infra.session import UserSession

from ..schemas.user_schema import User, UserCreate, UserUpdate
from ..controller.session_controller import get_session
from ..controller.user_controller import UserController

router = APIRouter(
    prefix = "/users",
    tags = ["User"],
    responses = {
        404: {
            "description" : "Not Found"
        }
    }
)

@router.post("/", response_model = User)
async def new_user(user: UserCreate, session: UserSession = Depends(get_session)):
    controller = UserController(session)
    return await controller.new_user(user, session)

@router.get("/", response_model = List[User])
async def get_users(session: UserSession = Depends(get_session)):
    controller = UserController(session)
    users = await controller.get_users(session)
    return users

@router.get("/{id}", response_model = User)
async def get_user_by_id(id: int, session: UserSession = Depends(get_session)):
    controller = UserController(session)
    user = await controller.get_user_by_id(id, session)
    if user is None:
        raise HTTPException(404)
    return user

@router.put("/{id}", response_model = User)
async def update_user(id: int, user: UserUpdate, session: UserSession = Depends(get_session)):
    controller = UserController(session)
    return await controller.update_user(id, user, session)

@router.delete("/{id}", response_model = User)
async def delete_user(id: int, session: UserSession = Depends(get_session)):
    controller = UserController(session)
    try:
        controller.delete_user(id)
    except:
        raise HTTPException(404)        