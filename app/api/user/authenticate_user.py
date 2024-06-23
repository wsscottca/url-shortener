''' Module contains function to authenticate the user '''

from app.api.auth.verify_password import verify_password
from app.api.exceptions import CredentialError
from app.db.services.get_user import get_user
from app.db.models.user import User


def authenticate_user(username: str, password: str) -> User:
    '''
    Validates the user's password
    
    Args:
        username (str): username of user to authenticate
        password (str): password of user to authenticate

    Raises:
        CredentialError: Invalid password
        
    Returns:
        User: The authenticated
    '''
    user = get_user(username)
    if not verify_password(password, user.password):
        raise CredentialError(401, "Invalid Password.")

    return user
