''' Module creates the tables for the DB models '''

from app.db.models.url_pair import UrlPair
from app.db.models.user import User

def create_table(item: User | UrlPair) -> None:
    ''' Check if the table exists, if not create it'''
    if not item.exists():
        item.create_table(wait=True, read_capacity_units=1, write_capacity_units=1)

# CREATE TABLES
# url_pairs table
create_table(UrlPair)
create_table(User)
