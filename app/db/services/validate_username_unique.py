from api import exceptions
from db.models.user import User


def validate_user_unique(username: str) -> str:
    '''
    Validates a user does not already exist

    Args:
    username (str): username to validate

    Raises:
    KeyExistsError: Provided username causes a collision

    Returns:
    str: Valid username that does not cause a collision
    '''
    # Validate if the provided username does not exist in the DB
    # If it does, raise a KeyExistsError
    try:
        User.get(username)
    except User.DoesNotExist:
        return username
    else:
        raise exceptions.KeyExistsError(422, "Username already exists, please select a different username.")