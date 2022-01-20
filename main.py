"""
App's entry point
"""
from fastapi import FastAPI

from api import router
from data.database.engine import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)
