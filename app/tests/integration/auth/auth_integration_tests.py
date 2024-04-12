from tests.integration.auth.password import test_hash_password, test_verify_password
from tests.integration.auth.token import test_create_token, test_token

def auth_integration_tests(client):
    test_hash_password()
    test_verify_password()

    test_create_token()
    test_token(client)