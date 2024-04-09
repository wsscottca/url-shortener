from api.auth.hash_password import hash_password
from api.user.authenticate_user import authenticate_user
from db.models.user import User


def test_authenticate_user():
    # Validate that our authenticate user properly validates
    # the password and gets our user
    user = authenticate_user("test", "test")
    assert type(user) == User
    assert user.username == "test"

def test_authenticate_user_invalid():
    # Test that if an authentication fails we return False
    result = authenticate_user("test1", hash_password("test2"))
    assert result == False