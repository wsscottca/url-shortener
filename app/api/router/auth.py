''' Module includes routes related to Authorization '''

from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.auth.create_token import create_token
from app.api.auth.dependencies import TOKEN_EXPIRE_MINUTES
from app.api.exceptions import InputError
from app.api.models.token import Token
from app.api.user.authenticate_user import authenticate_user

auth_router = APIRouter()

@auth_router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    '''
    Login route for user to log in and get a token for authorization

    Attributes:
        form_data (OAuth2PasswordRequestForm): Form data containing
            Username and Password for the Password OAuth2 flow

    Raises:
        InputError: Username or password were not within the alloted length

    Returns:
        Token: JWT for Authorization
    '''
    if 4 > len(form_data.username) or len(form_data.username) > 16:
        raise InputError(detail=
                         "Username not within length bounds. "
                         "Username must be between 4-16 characters.")
    if 8 > len(form_data.password) or len(form_data.password) > 32:
        raise InputError(detail=
                         "Password not within length bounds. "
                         "Password must be between 8-32 characters.")

    user = authenticate_user(form_data.username, form_data.password)
    token_expiration = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    token = create_token(data={"sub": user.username}, expires_delta=token_expiration)
    return Token(access_token=token, token_type="bearer")
