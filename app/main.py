from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session

from models.student import Student
from database.database import Base, engine, get_db
from routers.student import router as router_student

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusCore API",
    description="ERP Backend built with FastAPI",
    version="0.1.0"
)

app.include_router(router_student)

@app.get("/")
def home():
    return {
        "message": "Welcome to CampusCore 🚀"
    }


    