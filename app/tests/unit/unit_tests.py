from tests.unit.api.api_unit_tests import api_unit_tests
from tests.unit.auth.auth_unit_tests import auth_unit_tests
from tests.unit.db.db_unit_tests import db_unit_tests
from tests.unit.user.user_unit_tests import user_unit_tests


def unit_tests():
    api_unit_tests()
    auth_unit_tests()
    db_unit_tests()
    user_unit_tests()