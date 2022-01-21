from pydantic import BaseModel


class Group(BaseModel):
    name: str

    class Config:
        orm_mode = True


class GroupGet(Group):
    id: int

    class Config:
        orm_mode = True


class GroupCreate(Group):
    class Config:
        orm_mode = True
