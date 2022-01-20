from pydantic import BaseModel


class Group(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
