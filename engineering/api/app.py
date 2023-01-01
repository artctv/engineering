from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import *
from config import settings



app: FastAPI = FastAPI(
    title=settings.api.title,
    version=settings.api.version,
    description=settings.api.description
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.api.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
app.include_router(router)


