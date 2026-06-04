from fastapi import APIRouter
test_router = APIRouter(prefix="/test", tags=["test"])
from services.test_service import *

@test_router.get("/")
def test():
    users =  fetch_all_users()
    print (users)
    return({"users": users})

@test_router.get("/{name}")
def read_item(name: str):
    response =  fetch_user(name)
    return {"response": response}

@test_router.put("/{name}")
def read_item(name: str):
    response =  insert_user(name)
    return {"response": response}