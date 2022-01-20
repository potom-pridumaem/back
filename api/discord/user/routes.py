"""
User API for Discord
"""
from data.database import crud
from data.database.engine import get_db
from fastapi import APIRouter, Depends, HTTPException
from models.user import UserGet
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
    raise HTTPException(404, "User Not Found")
