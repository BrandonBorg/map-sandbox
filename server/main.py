from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from database.connection import init_db
from api.router import api_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    GZipMiddleware
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(api_router)