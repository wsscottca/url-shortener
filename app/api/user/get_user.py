import api.exceptions as ex
from db.models.user import User

async def get_user(username: str) -> User:
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
    except User.DoesNotExist:
        raise ex.KeyError(422, "User does not exist.")