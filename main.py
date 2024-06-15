from fastapi import FastAPI
from src.connection.connection import create_tables
from src.routes.user_route import routes_user

app = FastAPI()

app.include_router(routes_user, prefix="/user")

create_tables()