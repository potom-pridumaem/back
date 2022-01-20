from models.user import UserCreate
from sqlalchemy.orm import Session

from ..tables import User, UserGroup


def create(db: Session, user: UserCreate):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(db: Session, id: int):
    return db.query(User).get(id)


def get_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_by_discord_id(db: Session, discord_id: int):
    return db.query(User).filter(User.discord_id == discord_id).first()
