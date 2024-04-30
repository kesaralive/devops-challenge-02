import os
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Simple FastAPI service")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def say_hello():
    return {"message": "Hello from python-fastapi-service!"}

@app.get("/health")
def say_hello():
    return {"message": "ok"}

@app.on_event("startup")
async def startup():
    print("FastAPI is starting...")


@app.on_event("shutdown")
async def shutdown():
    print("FastAPI Service is shutting down...")


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.getenv("POST", "8000")), reload=True, root_path="/fastapi")
