from shortuuid import ShortUUID
from models.url_pair import Url_Pair
from api import exceptions

def validate_short_url(short_url: str | None) -> str:
     if not short_url:
        # If not provided a short_url, generate a valid one
        short_url = generate_short_url()
        return short_url

     else:
        try:
            Url_Pair.get(short_url)
        except Url_Pair.DoesNotExist:
            return short_url
        else:
            raise exceptions.KeyExistsError(422, "Short URL already exists, please enter a new short URL.")

def generate_short_url(validate: bool = True) -> str:
            short_url = None

            # Generate a shortuuid until we found one that isn't already in use
            while not short_url:
                try:
                    short_url = ShortUUID().random(length=8)
                    if validate:
                        validate_short_url(short_url)
                    return short_url
                except exceptions.KeyError:
                    short_url = None