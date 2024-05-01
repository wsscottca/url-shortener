''' Module contains function to generate a short url '''

from shortuuid import ShortUUID
from app.api import exceptions
from app.db.services.validate_url_unique import validate_url_unique

def generate_short_url() -> str:
    '''
    Generates a valid short url that does not cause a collision

    Returns:
    str: Valid generated short url that does not cause a collision
    '''
    short_url = None

    # Generate a shortuuid until we found one that isn't already in use
    while not short_url:
        try:
            short_url = ShortUUID().random(length=8)
            short_url = validate_url_unique(short_url)
            return short_url
        except exceptions.KeyExistsError:
            short_url = None

    return short_url
