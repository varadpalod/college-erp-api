from fastapi import FastAPI

app = FastAPI(
    title="CampusCore API",
    description="ERP Backend built with FastAPI",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CampusCore 🚀"
    }