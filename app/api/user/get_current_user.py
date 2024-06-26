''' Module provides the function required by the route to get the user from the token '''

from typing import Annotated
from fastapi import Depends
from jose import JWTError

from app.api.auth.decode_token import decode_token
from app.api.exceptions import CredentialError
from app.api.models.token import TokenData
from app.db.models.user import User
from app.db.services.get_user import get_user
from app.api.auth.dependencies import oauth2_scheme

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    '''
    Gets the current User from the DB
    
    Args:
        token (str): jwt token that depends OAuth2 flow for authentication
            using a bearer token obtained with a password

    Raises:
        CredentialError: Invalid credentials

    Returns:
        User: The current user
    '''
    try:
        # Decode the token to get the data
        payload = decode_token(token)
        # Get the username from the decoded payload
        username: str = payload.get("sub")
        # If there is no username, throw a credential error
        if username is None:
            raise CredentialError(401, "No user found in token.")
        token_data = TokenData(username=username)

    except JWTError as ex:
        # If there is an authentication error, throw a credential error
        raise CredentialError(401, repr(ex)) from ex

    # If we successfully get the username from the token, get the user from the db
    user = get_user(username=token_data.username)
    return user
