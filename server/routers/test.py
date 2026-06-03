from fastapi import APIRouter

TestRouter = APIRouter()

@TestRouter.get("/test")
async def test():
    return({"test":"works"})