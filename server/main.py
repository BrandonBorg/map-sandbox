from fastapi import FastAPI
from core.db import Database
from routers.test import TestRouter
app = FastAPI()

@app.on_event("startup")
def startup():
    app.state.db = Database()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q":q}

app.include_router(TestRouter)