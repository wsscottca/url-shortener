''' Module provides a create token function used for authorization '''

from datetime import datetime, timezone, timedelta
from jose import jwt

from app.api.auth.dependencies import ALGORITHM, SECRET_KEY


def create_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)) -> str:
    '''
    Creates a JWT token based on the data with expiration 

    Args:
    data (dict): Data to encode
    expires_delta (timedelta): Time for expiration

    Returns:
    str: Encoded JWT token
    '''
    to_encode = data.copy()
    # get the UTC time for expiration
    expires = datetime.now(timezone.utc) + expires_delta

    # add expiration to data to encode
    to_encode.update({"exp": expires})
    token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return token
