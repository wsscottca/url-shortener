''' Module includes function to run auth related integration tests '''

from app.tests.integration.auth.password import (test_hash_password,
    test_hash_password_empty_string, test_hash_password_no_input, test_verify_password)
from app.tests.integration.auth.token import (test_create_token,
    test_create_token_expired, test_decode_token, test_decode_token_expired,
    test_decode_token_modified, test_token, test_token_invalid_content_type,
    test_token_invalid_password_long, test_token_invalid_password_short,
    test_token_invalid_username_long, test_token_invalid_username_short,
    test_token_missing_password, test_token_missing_username, test_token_wrong_grant)

def auth_integration_tests(client):
    ''' Function for all auth related integration tests '''
    test_hash_password()
    test_hash_password_no_input()
    test_hash_password_empty_string()

    test_verify_password()

    test_create_token()
    test_create_token_expired()
    test_decode_token()
    test_decode_token_expired()
    test_decode_token_modified()

    test_token(client)
    test_token_missing_username(client)
    test_token_missing_password(client)
    test_token_invalid_content_type(client)
    test_token_wrong_grant(client)

    test_token_invalid_username_short(client)
    test_token_invalid_username_long(client)
    test_token_invalid_password_short(client)
    test_token_invalid_password_long(client)
