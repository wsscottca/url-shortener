''' User unit tests'''
from app.tests.unit.user.authenticate_user import (test_authenticate_user,
    test_authenticate_user_invalid)
from app.tests.unit.user.create_user import test_signup, test_signup_collision
from app.tests.unit.user.get_user import test_get_user, test_get_user_no_user
from app.tests.unit.user.validate_permissions import (test_validate_permissions,
    test_validate_permissions_invalid)

def user_unit_tests():
    ''' Runs all user related unit tests '''
    test_validate_permissions()
    test_validate_permissions_invalid()

    #pylint: disable=no-value-for-parameter
    test_get_user()
    test_get_user_no_user()

    test_authenticate_user()
    test_authenticate_user_invalid()

    test_signup()
    test_signup_collision()
    #pylint: enable=no-value-for-parameter
