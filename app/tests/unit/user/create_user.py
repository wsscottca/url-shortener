from unittest.mock import patch
import pytest
from api import exceptions
from api.router.user import create_user

@patch('api.router.user.User')
@patch('api.router.user.validate_user_unique')
@patch('api.router.user.hash_password')
def test_signup(mock_hash, mock_validate, mock_user):
    # Mock our dependencies
    # Fake hash mock
    mock_hash.return_value = "######"
    # Fake valid username mock
    mock_validate.return_value = "test1"
    # Fake dict response from DB
    mock_user.save.return_value = {"mocked": True}

    json_dict = create_user(username = "test1", password = "test1")
    mock_hash.assert_called_once_with("test1")
    mock_validate.assert_called_once_with("test1")
    #mock_user.save.assert_called_once()

    # Ensure the proper items are in our return
    assert "username" in json_dict
    assert json_dict["msg"] == "User created successfully"

@patch('api.router.user.User')
@patch('api.router.user.validate_user_unique')
@patch('api.router.user.hash_password')
def test_signup_collision(mock_hash, mock_validate, mock_user):
    # Mock our dependencies
    # Fake hash mock
    mock_hash.return_value = "######"
    # Mock throwing a validation error because the user "already exists"
    mock_validate.side_effect = exceptions.KeyExistsError(422, "Username already exists, please select a different username.")
    # Fake dict response from DB
    mock_user.save.return_value = {"mocked": True}

    # Ensure our function raises the proper error
    with pytest.raises(exceptions.KeyExistsError):
        create_user(username = "test1", password = "test1")