''' Unit tests for verify_password function '''

from unittest.mock import patch

from app.api.auth.verify_password import verify_password


@patch('app.api.auth.verify_password.password_context')
def test_verify_password(mocked_context):
    ''' Test verifying a password successfully '''
    # Mock our verification to test the hash is correct and responds appropriately
    mocked_context.verify.return_value = True
    password = "test"
    hashed_password = "$2b$12$.FDIB5slObexXIGvn/u2huruXUGNEdlvu3Or4JZIpWpuwFTOTJXR."
    verified = verify_password(password, hashed_password)
    mocked_context.verify.assert_called_once_with(password, hashed_password)
    assert verified == True

@patch('app.api.auth.verify_password.password_context')
def test_verify_password_invalid(mocked_context):
    ''' Test rejected a password that is incorrect '''
    # Mock our verification to test the hash is correct and responds appropriately
    # Even when the passwords do not match and therefore cannot be verified
    mocked_context.verify.return_value = False
    password = "test1"
    hashed_password = "$2b$12$.FDIB5slObexXIGvn/u2huruXUGNEdlvu3Or4JZIpWpuwFTOTJXR."
    verified = verify_password(password, hashed_password)
    mocked_context.verify.assert_called_once_with(password, hashed_password)
    assert verified is False
