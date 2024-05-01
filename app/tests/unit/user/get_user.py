''' Unit tests for getting current user '''

from datetime import datetime, timezone
from unittest.mock import patch

import pytest

from app.api.exceptions import CredentialError
from app.api.user.get_current_user import get_current_user
from app.db.models.user import User

@patch('app.api.user.get_current_user.get_user')
@patch('app.api.user.get_current_user.decode_token')
def test_get_user(mock_decode, mock_get_user):
    ''' Test successfully getting the current user '''
    # Mock decoding a token and recieving the payload
    mock_decode.return_value = {"sub": "test", "exp": datetime.now(timezone.utc)}
    # Mock getting a user from our DB
    mock_get_user.return_value = User(username="test",
        password="$2b$12$.FDIB5slObexXIGvn/u2huruXUGNEdlvu3Or4JZIpWpuwFTOTJXR.",
        group="user", disabled=False)

    user = get_current_user("faketoken")
    mock_decode.assert_called_once()
    mock_get_user.assert_called_once()

    # Ensure we got the proper user
    assert isinstance(user, User)
    assert user.username == "test"
    assert user.group == "user"

@patch('app.api.user.get_current_user.decode_token')
def test_get_user_no_user(mock_decode):
    ''' Test trying to get a user with a token missing the user '''
    # Mock decoding a token without a subject
    mock_decode.return_value = {"exp": datetime.now(timezone.utc)}

    # As there is no user we cant authenticate and throw an error
    with pytest.raises(CredentialError):
        get_current_user("faketoken")
