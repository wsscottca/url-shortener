from db.models.url_pair import Url_Pair
import api.exceptions as exceptions

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
        url_pair = Url_Pair.get(short_url)
        return url_pair.url
    except Url_Pair.DoesNotExist:
        raise exceptions.KeyError(422, "Short url does not exist.")