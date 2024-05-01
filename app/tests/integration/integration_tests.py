''' All integration tests '''
from fastapi.testclient import TestClient
from app.tests.integration.api.api_integration_tests import api_integration_tests
from app.tests.integration.auth.auth_integration_tests import auth_integration_tests
from app.tests.integration.db.db_integration_tests import db_integration_tests
from app.tests.integration.user.user_integration_tests import user_integration_tests

def integration_tests(client: TestClient):
    ''' Runs all categories of integration tests '''
    db_integration_tests()
    api_integration_tests(client)
    auth_integration_tests(client)
    user_integration_tests(client)
