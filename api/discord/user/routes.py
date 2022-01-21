"""
User API for Discord
"""
from data.database import crud
from data.database.engine import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import UserCreate, UserGet
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{discord_id}", response_model=UserGet)
def get_user(discord_id: int, db: Session = Depends(get_db)):
    """
    Get user by discord_id
    """
    user = crud.user.get_by_discord_id(db, discord_id)
    if user:
        return user
    raise HTTPException(status.HTTP_404_NOT_FOUND, "User Not Found")


@router.post("/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Register new user
    """
    user = crud.user.get_by_username(db, user_data.username)
    if not user:
        user = crud.user.create(db, user_data)
        return user
    raise HTTPException(status.HTTP_409_CONFLICT, "User already exists")
