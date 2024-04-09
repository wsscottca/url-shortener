from fastapi.testclient import TestClient
from tests.integration.api.api_integration_tests import api_integration_tests
from tests.integration.auth.auth_integration_tests import auth_integration_tests
from tests.integration.user.user_integration_tests import user_integration_tests

def integration_tests(client: TestClient):
    api_integration_tests(client)
    auth_integration_tests(client)
    user_integration_tests(client)