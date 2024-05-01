''' Authorization related unit tests '''
from app.tests.unit.auth.hash_password import test_hash_password
from app.tests.unit.auth.verify_password import test_verify_password, test_verify_password_invalid


def auth_unit_tests():
    ''' Runs authorization related unit tests '''
    #pylint: disable=no-value-for-parameter
    test_hash_password()
    test_verify_password()
    test_verify_password_invalid()
    #pylint: enable=no-value-for-parameter
