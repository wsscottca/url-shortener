''' Module includes DB service for validating a short URL is unique '''

from app.api.exceptions import KeyExistsError
from app.db.models.url_pair import UrlPair


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
        UrlPair.get(short_url)
        # If we get a pair from the short URL we would have a collision if adding it again
        raise KeyExistsError(422, "Short URL already exists, please enter a new short URL.")
    except UrlPair.DoesNotExist:
        return short_url
