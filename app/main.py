from .routers import business, login,talent, subscribe
from . import models
from fastapi import FastAPI
from .database import engine
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(subscribe.router)
app.include_router(business.router)
app.include_router(talent.router)
app.include_router(login.router)










