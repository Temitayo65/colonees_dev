from .routers import business, login,talent, subscribe
from . import models
from fastapi import FastAPI
from .database import engine
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"] # put only http://www.colonees.com here 

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(subscribe.router)
app.include_router(business.router)
app.include_router(talent.router)
app.include_router(login.router)










