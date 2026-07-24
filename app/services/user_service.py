from sqlalchemy.orm import Session
from fastapi import HTTPException 
from schemas.user import UserCreate
from models.user import User
from utils import security
def get_users(db:Session):
    users=db.query(User).all()
    return users

def create_user(db:Session,user:UserCreate):
    existing_user=db.query(User).filter(user.username==User.username).first()
    if existing_user is not None:
        raise HTTPException(status_code=400,detail="User Name Exists")
    db_user = User(username=user.username,hashed_password=security.hash_password(user.password),role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def update_user(db:Session,user:UserCreate,id:int):
    existing_user=db.query(User).filter(User.id==id).first()
    if existing_user is None:
        raise HTTPException(status_code=404,detail="id does not exist")

    existing_user.username=user.username
    existing_user.hashed_password=security.hash_password(user.password)
    existing_user.role=user.role

    db.commit()
    db.refresh(existing_user)
    return existing_user

def delete_user(id:int,db:Session):
    existing_user=db.query(User).filter(User.id==id).first()
        
    if(existing_user is None):
        raise HTTPException(status_code=404,detail="ID not found")
        
    db.delete(existing_user)
    db.commit()
    return "deletion suucesfull"
        