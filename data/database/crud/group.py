from models.group import GroupCreate, GroupGet
from sqlalchemy.orm import Session

from ..tables import Group, UserGroup


def get(db: Session, id: int):
    return db.query(Group).get(id)


def create(db: Session, group: GroupCreate):
    new_group = Group(**group.dict())
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group
