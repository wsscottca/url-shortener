''' Module for DB unit tests '''
from app.tests.unit.db.empty_database import test_empty_database
from app.tests.unit.db.update_item import test_add_url_pair

def db_unit_tests():
    ''' Runs DB Unit Tests '''
    test_empty_database()
    test_add_url_pair()
