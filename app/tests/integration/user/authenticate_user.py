''' Integration tests for authenticate user '''
import pytest
from app.api.auth.hash_password import hash_password
from app.api.exceptions import CredentialError
from app.api.user.authenticate_user import authenticate_user
from app.db.models.user import User


def test_authenticate_user():
    ''' Validate that our authenticate user properly validates
    the password and gets our user'''
    user = authenticate_user("test", "password")
    assert isinstance(user, User)
    assert user.username == "test"

def test_authenticate_user_invalid():
    '''Test that if an authentication fails we return False'''
    # Ensure our function raises the proper error
    with pytest.raises(CredentialError):
        authenticate_user("test1", hash_password("test2"))
