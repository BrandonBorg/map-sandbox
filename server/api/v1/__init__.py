from fastapi import APIRouter
from api.v1.test import test_router

v1_router = APIRouter()

v1_router.include_router(test_router)