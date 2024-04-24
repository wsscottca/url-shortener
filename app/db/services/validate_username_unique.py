''' Module contains DB service for if a user is unique '''

from app.api import exceptions
from app.db.models.user import User


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
        # if we get a user from the username we cannot enter a new user without causing a collision
        raise exceptions.KeyExistsError(422,
                                "Username already exists, please select a different username.")
    except User.DoesNotExist:
        return username
