''' Module provides a decode token function used for authorization '''

from typing import Any
from jose import jwt
from app.api.auth.dependencies import ALGORITHM, SECRET_KEY


def decode_token(token: str) -> dict[str, Any]:
    '''
    Decodes a JWT Token and returns the data

    Args:
    token (str): Token to decode

    Returns:
    dict: Decoded payload
    '''
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
