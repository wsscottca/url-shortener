from fastapi.testclient import TestClient
from tests.integration.integration_tests import integration_tests
from tests.unit.unit_tests import unit_tests

def perform_tests(app):
    client = TestClient(app)
    unit_tests()
    integration_tests(client)