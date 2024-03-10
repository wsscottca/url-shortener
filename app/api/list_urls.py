from typing import Dict
from models.url_pair import Url_Pair, Url_Pair_VM

def get_urls() -> Dict[int, Url_Pair_VM]:
    '''
    Return all short url - original url pairs currently in the DB
    
    Returns:
        Dict[int, Url_Pair_VM]: All short url - original url pairs, indexed
    '''
    url_pairs = {}
    index = 0

    # Get all pairs from DB and add to our dict
    for url_pair in Url_Pair.scan():
        url_pairs[index] = url_pair
        index += 1

    return url_pairs