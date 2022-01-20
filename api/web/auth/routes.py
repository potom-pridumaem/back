from data.database import crud
from data.database.engine import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT
from models.auth import Token
from sqlalchemy.orm import Session
from utils import auth

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", response_model=Token)
async def login(
    credentials: OAuth2PasswordRequestForm = Depends(),
    Authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    user = crud.user.get_by_username(db, credentials.username)
    if user:
        if auth.verify_password(credentials.password, user.password):
            access_token = Authorize.create_access_token(user.id)
            return Token(access_token=access_token)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
    )
