import logging
from unittest.mock import patch
from api.auth.hash_password import hash_password

@patch('api.auth.hash_password.password_context')
def test_hash_password(mocked_context):
    # Set up mock of an example hashed password from outside library
    mocked_context.hash.return_value = "$2b$12$.FDIB5slObexXIGvn/u2huruXUGNEdlvu3Or4JZIpWpuwFTOTJXR."
    hashed_password = hash_password("test")
    mocked_context.hash.assert_called_once()
    # Validate that our hash function properly passes back the created hash
    assert hashed_password == "$2b$12$.FDIB5slObexXIGvn/u2huruXUGNEdlvu3Or4JZIpWpuwFTOTJXR."