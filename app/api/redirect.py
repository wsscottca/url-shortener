from models.url_pair import Url_Pair
import api.exceptions as exceptions

def get_redirect_url(short_url: str) -> str:
    # Get original URL if short_url in DB otherwise throw KeyError
    try:
        url_pair = Url_Pair.get(short_url)
        return url_pair.url
    except Url_Pair.DoesNotExist:
        raise exceptions.KeyError(422, "Short url does not exist.")