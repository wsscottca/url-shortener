from pydantic import BaseModel
from db.models.url_pair import Url_Pair
from db.models.user import User

def create_table(item: BaseModel) -> None:
    ''' Check if the table exists, if not create it'''
    if not item.exists():
        item.create_table(wait=True, read_capacity_units=1, write_capacity_units=1)

''' CREATE TABLES '''
# url_pairs table
create_table(Url_Pair)
create_table(User)
