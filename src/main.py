from typing import Union

from fastapi import FastAPI

from .routes.circle import router as circle_router
from .routes.user_routes import router as user_router

app = FastAPI()

app.include_router(circle_router, user_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}