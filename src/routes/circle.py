from typing import List
from fastapi import APIRouter, HTTPException
from schemas.circle import Circle, CircleCreate
from controller.circle_controller import CircleController as controller

router = APIRouter(
    prefix = "/circles",
    tags = ["Circle"],
    responses={404: {"description": "Not found"}},
)

@router.put("/", response_model=Circle)
async def new_circle(circle: CircleCreate):
    return await controller.save(circle)

@router.get("/", response_model=List[Circle])
async def get_circles():
    circles = await controller.get_all()
    return circles

@router.get("/{id}", response_model=Circle)
async def get_circle_by_id(id: int):
    circle = await controller.find(id)
    if circle is None:
        raise HTTPException(404)
    return circle
