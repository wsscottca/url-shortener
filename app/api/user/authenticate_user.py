from api.auth.verify_password import verify_password
from db.services.get_user import get_user
from db.models.user import User


def authenticate_user(username: str, password: str) -> User | bool:
    '''
    Validates the user's password
    
    Args:
        username (str): username of user to authenticate
        password (str): password of user to authenticate

    Returns:
        User: The authenticated
        bool: False if the user cannot be authenticated
    '''
    user = get_user(username)
    if not verify_password(password, user.password):
        return False
    
    return user