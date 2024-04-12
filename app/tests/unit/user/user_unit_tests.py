
from tests.unit.user.authenticate_user import test_authenticate_user, test_authenticate_user_invalid
from tests.unit.user.create_user import test_signup, test_signup_collision
from tests.unit.user.get_user import test_get_user, test_get_user_no_user
from tests.unit.user.validate_permissions import test_validate_permissions, test_validate_permissions_invalid

def user_unit_tests():
    test_validate_permissions()
    test_validate_permissions_invalid()

    test_get_user()
    test_get_user_no_user()

    test_authenticate_user()
    test_authenticate_user_invalid()

    test_signup()
    test_signup_collision()