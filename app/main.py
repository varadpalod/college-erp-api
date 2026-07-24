from fastapi import FastAPI
from database.database import Base, engine
from routers.student import router as router_student
from routers.attendance import router as router_attendance
from routers.user import router as router_user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusCore API",
    description="ERP Backend built with FastAPI",
    version="0.1.0"
)

app.include_router(router_student)
app.include_router(router_attendance)
app.include_router(router_user)

@app.get("/")
def home():
    return {
        "message": "Welcome to CampusCore 🚀"
    }


    