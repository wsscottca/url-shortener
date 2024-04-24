''' Module contains function for performing all tests '''

from fastapi.testclient import TestClient
from app.tests.integration.integration_tests import integration_tests
from app.tests.unit.unit_tests import unit_tests

def perform_tests(app):
    ''' Main tests function, runs integration and unit tests '''
    client = TestClient(app)
    unit_tests()
    integration_tests(client)
