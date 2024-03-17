from shortuuid import ShortUUID
from models.url_pair import Url_Pair
from api import exceptions

def validate_short_url(short_url: str | None) -> str:
    '''
    Validates a short url or generates a valid short url if one is not provided

    Args:
    short_url (str): Short url to validate or None if one needs to be generated

    Raises:
    KeyExistsError: Provided short url causes a collision

    Returns:
    str: Valid short url that does not cause a collision
    '''
    if not short_url:
        # If not provided a short_url, generate a valid one
        # generate_short_url() calls this function to validate
        # so we do not need additional validation
        short_url = generate_short_url()
        return short_url

    # Validate if the provided or generated short url already exists
    # If it does, raise a KeyExistsError
    try:
        Url_Pair.get(short_url)
    except Url_Pair.DoesNotExist:
        return short_url
    else:
        raise exceptions.KeyExistsError(422, "Short URL already exists, please enter a new short URL.")

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
            short_url = validate_short_url(short_url)
            return short_url
        except exceptions.KeyExistsError:
            short_url = None