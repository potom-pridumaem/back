from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    discord_id: int | None = None

    class Config:
        orm_mode = True


class UserGet(User):
    id: int

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str

    class Config:
        orm_mode = True
