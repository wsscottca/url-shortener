from tests.unit.db.create_table import test_empty_database
from tests.unit.db.update_item import test_add_url_pair

def db_unit_tests():
    test_empty_database()
    test_add_url_pair()