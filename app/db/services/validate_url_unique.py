from api import exceptions
from db.models.url_pair import Url_Pair


def validate_url_unique(short_url: str) -> str:
    '''
    Validates a short url does not already exist

    Args:
    short_url (str): Short url to validate

    Raises:
    KeyExistsError: Provided short url causes a collision

    Returns:
    str: Valid short url that does not cause a collision
    '''
    # Validate if the provided or generated short url already exists
    # If it does, raise a KeyExistsError
    try:
        Url_Pair.get(short_url)
    except Url_Pair.DoesNotExist:
        return short_url
    else:
        raise exceptions.KeyExistsError(422, "Short URL already exists, please enter a new short URL.")