import os
from functools import partial

from tortoise.contrib.fastapi import RegisterTortoise

register_orm = partial(
    RegisterTortoise,
    db_url=os.getenv("DB_URL", "sqlite://crm.db"),
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

TORTOISE_ORM = {
    "connections": {"default": "sqlite://crm.db"},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}