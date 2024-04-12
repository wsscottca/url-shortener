from fastapi.testclient import TestClient

from tests.integration.user.authenticate_user import test_authenticate_user, test_authenticate_user_invalid
from tests.integration.user.create_user import test_signup, test_signup_invalid
from tests.integration.user.get_user import test_get_user

def user_integration_tests(client: TestClient):

    test_signup(client)
    test_signup_invalid(client)

    test_authenticate_user()
    test_authenticate_user_invalid()

    test_get_user(client)