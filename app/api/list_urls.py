from typing import Dict
from models.url_pair import Url_Pair, Url_Pair_VM

def get_urls() -> Dict[int, Url_Pair_VM]:
    url_pairs = {}
    count = 0
    for url_pair in Url_Pair.scan():
        url_pairs[count] = url_pair
        count += 1

    return url_pairs