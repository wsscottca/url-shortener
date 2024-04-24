''' Authenticate user unit tests '''
from unittest.mock import patch

from app.api.user.authenticate_user import authenticate_user
from app.db.models.user import User

@patch('app.api.user.authenticate_user.verify_password')
@patch('app.api.user.authenticate_user.get_user')
def test_authenticate_user(mock_get, mock_validate):
    ''' Test authenticating a user successfully'''
    # Mock our get to return a user "from the db"
    mock_get.return_value = User(username="test",
        password="$2b$12$.FDIB5slObexXIGvn/u2huruXUGNEdlvu3Or4JZIpWpuwFTOTJXR.",
        group="user", disabled=False)
    # Mock our validate to be True
    mock_validate.return_value = True

    user = authenticate_user("test", "test")
    mock_validate.assert_called_once()
    mock_get.assert_called_once()

    # Ensure we recieved back the user, and that it is the proper user
    assert isinstance(user, User)
    assert user.username == "test"
    assert user.disabled is False

@patch('app.api.user.authenticate_user.verify_password')
@patch('app.api.user.authenticate_user.get_user')
def test_authenticate_user_invalid(mock_get, mock_validate):
    ''' Test a failed authentication '''
    # Mock our get to return a user "from the db"
    mock_get.return_value = User(username="test", password="test", group="user", disabled=False)
    # Mock our validate to be False as though the wrong password was given
    mock_validate.return_value = False

    authenticated = authenticate_user("test", "test")
    mock_validate.assert_called_once()
    mock_get.assert_called_once()

    # Ensure we did not authenicate the attempt
    assert authenticated is False
