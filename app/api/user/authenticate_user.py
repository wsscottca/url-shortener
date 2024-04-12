from api.auth.verify_password import verify_password
from api.user.get_user import get_user
from db.models.user import User


async def authenticate_user(username: str, password: str) -> User | bool:
    '''
    Gets the current User from the DB
    
    Args:
        token (str): jwt token that depends OAuth2 flow for authentication using a bearer token obtained with a password

    Returns:
        User: The current user
    '''
    user = await get_user(username)
    if not verify_password(password, user.password):
        return False
    
    return user