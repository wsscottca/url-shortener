from fastapi.testclient import TestClient

from tests.integration.user.authenticate_user import test_authenticate_user, test_authenticate_user_invalid
from tests.integration.user.create_user import test_signup, test_signup_invalid, test_signup_invalid_content_type, test_signup_long_password, test_signup_long_username, test_signup_missing_password, test_signup_missing_username, test_signup_short_password, test_signup_short_username
from tests.integration.user.get_user import test_get_user, test_get_user_expired, test_get_user_invalid

def user_integration_tests(client: TestClient):

    test_signup(client)
    test_signup_invalid(client)
    test_signup_missing_username(client)
    test_signup_missing_password(client)
    test_signup_invalid_content_type(client)
    test_signup_long_username(client)
    test_signup_long_password(client)
    test_signup_short_password(client)
    test_signup_short_username(client)

    test_authenticate_user()
    test_authenticate_user_invalid()

    test_get_user(client)
    test_get_user_expired(client)
    test_get_user_invalid(client)