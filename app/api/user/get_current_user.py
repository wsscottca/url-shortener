import logging
from typing import Annotated
from fastapi import Depends
from jose import JWTError

from api.auth.decode_token import decode_token
from api.exceptions import CredentialError
from api.models.token import TokenData
from db.models.user import User
from db.services.get_user import get_user
from api.auth.dependencies import oauth2_scheme

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    '''
    Gets the current User from the DB
    
    Args:
        token (str): jwt token that depends OAuth2 flow for authentication using a bearer token obtained with a password

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

    # TODO: Break Errors into specific errors and responses instead of using the broad JWTError
    except JWTError as ex:
        # If there is an authentication error, throw a credential error
        raise CredentialError(401, repr(ex))
    
    # If we successfully get the username from the token, get the user from the db
    user = get_user(username=token_data.username)
    return user