from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from api.auth.create_token import create_token
from api.auth.dependencies import TOKEN_EXPIRE_MINUTES
from api.models.token import Token
from api.user.authenticate_user import authenticate_user

auth_router = APIRouter()

@auth_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = await authenticate_user(form_data.username, form_data.password)
    token_expiration = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    token = create_token(data={"sub": user.username, "scopes": form_data.scopes}, expires_delta=token_expiration)
    return Token(access_token=token, token_type="bearer")