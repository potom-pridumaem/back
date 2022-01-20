"""
User API for Web
"""
from data.database import crud
from data.database.engine import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from models.user import User, UserCreate
from sqlalchemy.orm import Session
from utils import auth

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
def create(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Register new user
    """
    user = crud.user.get_by_username(db, user_data.username)
    if not user:
        user_data.password = auth.get_password_hash(user_data.password)
        user = crud.user.create(db, user_data)
        return user
    raise HTTPException(status.HTTP_409_CONFLICT, "User already exists")


@router.get("/me")
def get_me(subject: User = Depends(auth.get_subject)):
    return subject
