from typing import Any
from jose import jwt
from api.auth.dependencies import ALGORITHM, SECRET_KEY
from db.models.user import User


def decode_token(token: str) -> dict[str, Any]:
    '''
    Decodes a JWT Token and returns the data

    Args:
    token (str): Token to decode

    Returns:
    dict: Decoded payload
    '''
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)