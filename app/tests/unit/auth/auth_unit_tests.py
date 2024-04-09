from tests.unit.auth.hash_password import test_hash_password
from tests.unit.auth.verify_password import test_verify_password


def auth_unit_tests():
    test_hash_password()
    test_verify_password()
    