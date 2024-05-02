''' Module gets a user from the DB '''

import app.api.exceptions as ex
from app.db.models.user import User

def get_user(username: str) -> User:
    '''
    Gets a User from the DB
    
    Args:
        username (str): username key to fetch user from DB

    Raises:
        KeyError: Credential does not exist in the database

    Returns:
        User: The user attached to the username in the DB
    '''
    try:
        user = User.get(username)
        return user
    except User.DoesNotExist as exc:
        raise ex.KeyDoesNotExistError(422, "User does not exist.") from exc
