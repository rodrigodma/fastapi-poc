from typing import List
from fastapi import APIRouter, HTTPException
from models import circle
from controller.circle_controller import CircleController as controller

router = APIRouter()

Circle = circle.Circle

@router.put("/circle/", response_model=Circle, tags=["circle"])
async def new_circle(circle: Circle):
    return await controller.save(Circle)

@router.get("/circle/", response_model=List[Circle], tags=["circle"])
async def get_circles():
    circles = await controller.getAll()
    return circles

@router.get("/circle/{id}", response_model=Circle, tags=["hugs"])
async def get_circle_by_id(id: int):
    circle = await controller.find(id)
    if circle is None:
        raise HTTPException(404)
    return circle
