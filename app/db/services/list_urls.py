from typing import Dict

from api.models.url_pair import Url_Pair_VM
from db.models.url_pair import Url_Pair

def get_urls() -> Dict[int, Url_Pair_VM]:
    '''
    Return all short url - original url pairs currently in the DB
    
    Returns:
        Dict[int, Url_Pair_VM]: All short url - original url pairs, indexed
    '''
    url_pairs = {}
    index = 0

    try:
        # Get all pairs from DB and add to our dict
        db_content = Url_Pair.scan()
        if type(db_content) == BaseException:
            raise db_content
        for url_pair in db_content:
            url_pairs[index] = url_pair
            index += 1
    except:
        raise

    return url_pairs