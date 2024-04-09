from unittest.mock import patch
from api.auth.hash_password import hash_password
from api.user.authenticate_user import authenticate_user
from db.models.user import User

@patch('api.user.authenticate_user.verify_password')
@patch('api.user.authenticate_user.get_user')
def test_authenticate_user(mock_get, mock_validate):
    # Mock our get to return a user "from the db"
    mock_get.return_value = User(username="test", password="$2b$12$.FDIB5slObexXIGvn/u2huruXUGNEdlvu3Or4JZIpWpuwFTOTJXR.", group="user", disabled=False)
    # Mock our validate to be True
    mock_validate.return_value = True

    user = authenticate_user("test", "test")
    mock_validate.assert_called_once()
    mock_get.assert_called_once()

    # Ensure we recieved back the user, and that it is the proper user
    assert type(user) == User
    assert user.username == "test"
    assert user.disabled == False

@patch('api.user.authenticate_user.verify_password')
@patch('api.user.authenticate_user.get_user')
def test_authenticate_user_invalid(mock_get, mock_validate):
    # Mock our get to return a user "from the db"
    mock_get.return_value = User(username="test", password="test", group="user", disabled=False)
    # Mock our validate to be False as though the wrong password was given
    mock_validate.return_value = False

    authenticated = authenticate_user("test", "test")
    mock_validate.assert_called_once()
    mock_get.assert_called_once()

    # Ensure we did not authenicate the attempt
    assert authenticated == False