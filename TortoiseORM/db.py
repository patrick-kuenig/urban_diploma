from tortoise import Tortoise

db_url = "sqlite://crm.db"
modules = {'models': ['models']}

TORTOISE_ORM = {
    "connections": {"default": db_url},
    "apps": {
        "models": {
            "models": modules.get("models", []) + ["aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init():
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['models']}
    )

    await Tortoise.generate_schemas(safe=True)


async def migrate_db():
    await init()

    # Generate the schema
    await Tortoise.generate_schemas(safe=True)