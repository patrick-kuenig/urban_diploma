import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from routers import categories, customers, tasks, users

from config import register_orm
from tortoise import Tortoise, generate_config
from tortoise.contrib.fastapi import RegisterTortoise


@asynccontextmanager
async def lifespan_test(app: FastAPI) -> AsyncGenerator[None, None]:
    config = generate_config(
        os.getenv("TORTOISE_DB", "sqlite://:memory:"),
        app_modules={"models": ["models"]},
        testing=True,
        connection_label="models",
    )
    async with RegisterTortoise(
        app=app,
        config=config,
        generate_schemas=True,
        add_exception_handlers=True,
        _create_db=True,
    ):
        # db connected
        yield
        # app teardown
    # db connections closed
    await Tortoise._drop_databases()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    if getattr(app.state, "testing", None):
        async with lifespan_test(app) as _:
            yield
    else:
        # app startup
        async with register_orm(app):
            # db connected
            yield
            # app teardown
        # db connections closed


app = FastAPI(title="CRM_simple")


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello CRM'}

app.include_router(categories.router)
app.include_router(customers.router)
app.include_router(tasks.router)
app.include_router(users.router)
