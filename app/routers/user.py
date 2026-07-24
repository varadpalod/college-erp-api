from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session

from schemas.user import UserCreate,UserResponse
from models.user import User
from database.database import Base, engine, get_db
from services import user_service

router=APIRouter(prefix="/users",tags=["User"])

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.put("/{id}",response_model=UserResponse)
def update_user(id :int,user:UserCreate,db: Session=Depends(get_db)):
    return user_service.update_user(db,user,id)

@router.post("/",response_model=UserResponse)
def create_user(user :UserCreate,db:Session=Depends(get_db)):
    return user_service.create_user(db,user)

@router.delete("/{id}")
def remove_user( id:int,db:Session=Depends(get_db)):
    return user_service.delete_user(id,db)