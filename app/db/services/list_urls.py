''' Module containts supporting DB service for list_urls route. '''

from typing import Dict

from app.api.models.url_pair import UrlPairVM
from app.db.models.url_pair import UrlPair

def get_urls() -> Dict[UrlPairVM.short_url, UrlPairVM.url]:
    '''
    Return all short url - original url pairs currently in the DB
    
    Returns:
        Dict[int, Url_Pair_VM]: All short url - original url pairs, indexed
    '''
    url_pairs = {}

    # Get all pairs from DB and add to our dict
    db_content = UrlPair.scan()
    for url_pair in db_content:
        url_pairs[url_pair.short_url] = url_pair.url

    return url_pairs
