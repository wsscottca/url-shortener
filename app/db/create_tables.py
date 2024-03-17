from pydantic import BaseModel
from models.url_pair import Url_Pair

def create_table(item: BaseModel) -> None:
    ''' Check if the table exists, if not create it'''
    if not item.exists():
        item.create_table(wait=True, read_capacity_units=5, write_capacity_units=5)

''' CREATE TABLES '''
# url_pairs table
create_table(Url_Pair)
