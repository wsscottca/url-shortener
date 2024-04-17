import logging

import pytest
from api.auth.hash_password import hash_password
from api.auth.verify_password import verify_password


def test_hash_password():
    # Test that we are being returned a hashed password
    password = "test1"
    hashed_password = hash_password(password)
    assert hashed_password != password
    assert len(hashed_password) == 60

def test_hash_password_no_input():
    password = None

    with pytest.raises(TypeError):
        hash_password(password)

def test_hash_password_empty_string():
    # Test that we are being returned a hashed password
    password = ""
    hashed_password = hash_password(password)
    assert hashed_password != password
    assert len(hashed_password) == 60

def test_verify_password():
    # Ensure that our verification properly validates the hash against the original
    password = "test1"
    hashed_password = hash_password(password)
    assert verify_password(password, hashed_password) == True