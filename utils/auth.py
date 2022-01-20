from data.config.env import JWT_SECRET
from data.database import crud
from data.database.engine import get_db
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi_jwt_auth import AuthJWT
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer("/api/web/auth")


@AuthJWT.load_config
def get_config():
    class Settings(BaseModel):
        authjwt_secret_key: str = JWT_SECRET
    return Settings()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_subject(_: str = Depends(oauth2_scheme), Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()

    subject = Authorize.get_jwt_subject()
    user = crud.user.get(db, subject)
    return user
