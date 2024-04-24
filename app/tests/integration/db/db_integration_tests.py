''' Module tests failure in DB dependency '''

from app.tests.integration.db.connection import test_db_conn_failure
from app.tests.integration.db.delete import test_db_delete_failure
from app.tests.integration.db.get import test_db_get_failure
from app.tests.integration.db.save import test_db_save_failure
from app.tests.integration.db.scan import test_db_scan_failure
from app.tests.integration.db.table import test_db_create_table_failure


def db_integration_tests():
    ''' Integration tests for DB related functionality '''
    #pylint: disable=no-value-for-parameter
    test_db_conn_failure()
    test_db_create_table_failure()
    test_db_save_failure()
    test_db_get_failure()
    test_db_scan_failure()
    test_db_delete_failure()
    #pylint: enable=no-value-for-parameter
