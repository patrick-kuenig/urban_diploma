from fastapi import FastAPI
from routers import categories, customers, tasks, users

app = FastAPI()
# templates = Jinja2Templates(directory='TortoiseORM.templates')
# I chose not to modify/use templates in this project for now as the main topic are databases and ORMs

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Open /docs'}

app.include_router(categories.router)
app.include_router(customers.router)
app.include_router(tasks.router)
app.include_router(users.router)
