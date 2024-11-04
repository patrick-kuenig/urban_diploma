from fastapi import FastAPI
from fastapi import status
from fastapi import Body
from fastapi import HTTPException
from fastapi import Request
from fastapi import Path
from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from .routers import categories

app = FastAPI()
templates = Jinja2Templates(directory='TortoiseORM.templates')


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}

app.include_router(categories.router)