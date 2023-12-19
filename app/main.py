from fastapi.responses import HTMLResponse
from .routers import business, login,talent, subscribe, admin
from . import models
from fastapi import FastAPI
from .database import engine
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pathlib import Path



# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# put only https://www.colonees.com here
origins = ["https://api.colonees.com",
           "https://www.colonees.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse("""
                <!-- templates/base.html -->
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Colonees Team AI API</title>
                <style>
                    body {
                        font-family: 'Roboto', sans-serif;
                        margin: 40px;
                        text-align: center;
                        background-color: #f7f7f7;
                    }
                    h1 {
                        font-size: 2.5em;
                        color: #333;
                    }
                    p {
                        font-size: 1.2em;
                        color: #555;
                    }
                    footer {
                        margin-top: 20px;
                        font-size: 0.8em;
                        color: #777;
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the Colonees Team AI API</h1>
                <p>This API is powered by cutting-edge artificial intelligence technology. Explore the endpoints to experience the future of data science.</p>
                <footer>Generated by AI</footer>
            </body>
            </html>
        """)

app.include_router(subscribe.router)
app.include_router(business.router)
app.include_router(talent.router)
app.include_router(login.router)
app.include_router(admin.router)










