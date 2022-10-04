from fastapi import APIRouter, HTTPException

router = APIRouter()

Circle = models.Circle

@router.put("/circle/", response_model=Circle, tags=["circle"])
def new_circle(circle: Circle):
    return ''
