from tokenize import group

from data.database import crud
from data.database.engine import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models.group import GroupCreate, GroupGet
from sqlalchemy.orm import Session

router = APIRouter(prefix="/group", tags=["group"])


@router.get("/{group_id}", response_model=GroupGet)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = crud.group.get(db, group_id)
    if group:
        return group
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Group Not Found")


@router.post("/")
def create_group(group_data: GroupCreate, db: Session = Depends(get_db)):
    """
    Create new group
    """
    group = crud.group.create(db, group_data)
    return group
