from typing import List
from fastapi import APIRouter, HTTPException, Depends
from controller.circle_session_controller import CircleSessionController
from infra.session import CircleSession
from schemas.circle import Circle, CircleCreate
from controller.circle_controller import CircleController

router = APIRouter(
    prefix = "/circles",
    tags = ["Circle"],
    responses={404: {"description": "Not found"}},
)

session_controller = CircleSessionController()

@router.put("/", response_model=Circle)
async def new_circle(circle: CircleCreate, session: CircleSession = Depends(session_controller.get_session())):
    controller = CircleController(session)
    return await controller.save(circle, session)

@router.get("/", response_model=List[Circle])
async def get_circles(session: CircleSession = Depends(session_controller.get_session())):
    controller = CircleController(session)
    circles = await controller.get_all(session)
    return circles

@router.get("/{id}", response_model=Circle)
async def get_circle_by_id(id: int, session: CircleSession = Depends(session_controller.get_session())):
    controller = CircleController(session)
    circle = await controller.find(id, session)
    if circle is None:
        raise HTTPException(404)
    return circle
