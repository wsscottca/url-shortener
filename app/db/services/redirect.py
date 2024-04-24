''' Module contains DB service from getting the redirect url '''

from app.api.exceptions import KeyDoesNotExistError
from app.db.models.url_pair import UrlPair

def get_redirect_url(short_url: str) -> str:
    '''
    Gets the original url to redirect to when given a valid short url
    
    Args:
        short_url (str): Short url key to fetch original url from DB

    Raises:
        KeyError: Short url does not exist in the database

    Returns:
        str: The original url to redirect to
    '''
    try:
        url_pair = UrlPair.get(short_url)
        return url_pair.url
    except UrlPair.DoesNotExist as exc:
        raise KeyDoesNotExistError(422, "Short url does not exist.") from exc
