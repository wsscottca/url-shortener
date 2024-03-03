from models.url_pair import Url_Pair

''' CREATE TABLES '''
# url_pairs table
if not Url_Pair.exists():
    Url_Pair.create_table(wait=True, read_capacity_units=5, write_capacity_units=5)
