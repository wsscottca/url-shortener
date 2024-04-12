import pytest
from api.auth.hash_password import hash_password
from api.exceptions import CredentialError
from api.user.validate_permissions import validate_user_permissions
from db.models.user import User


def test_validate_permissions():
    hashed_password = hash_password("test1")
    user = User(username="test1", password=hashed_password, group="admin", disabled=False)
    validated = validate_user_permissions(user, "admin")

    # Validate that we're properly checking the required group and the user's group are valid
    assert validated == True

def test_validate_permissions_invalid():
    hashed_password = hash_password("test2")
    user = User(username="test2", password=hashed_password, group="user", disabled=False)

    # When the user's group is not correct validate that we throw a credential error
    with pytest.raises(CredentialError) as ex:
        validate_user_permissions(user, "admin")
        assert type(ex) == CredentialError
        assert ex.status_code == 401
        # Ensure the message is specific to this authorization issue
        assert ex.detail == "You do not have the appropriate permissions to access this route."
