from tortoise import Tortoise
from tortoise import run_async


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )

    await Tortoise.generate_schemas(safe=True)

run_async(init())
