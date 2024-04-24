''' Module contains routes for user functionality - creating/getting a user '''

from typing import Annotated

from fastapi import APIRouter, Depends, Form, Query
from app.api.auth.hash_password import hash_password
from app.api.models.user import UserVM
from app.api.user.get_current_user import get_current_user
from app.db.models.user import User
from app.db.services.validate_username_unique import validate_user_unique

user_router = APIRouter()

@user_router.post("/signup", status_code=201)
def create_user(username: Annotated[str, Query(max_length=16, min_length=4), Form()],
                password: Annotated[str, Query(max_length=32, min_length=8), Form()]):
    '''
    Register route for user to be created

    Attributes:
        username (str): Username form field - between 4-16 characters
        password (str): Password form field - between 8-32 characters

    Returns:
        JSON: Username of created user and a message confirming creation was successful
    '''
    hashed_password = hash_password(password)
    username = validate_user_unique(username)
    new_user = User(username, password=hashed_password, group="user", disabled=False)
    new_user.save()
    return {
        "username": new_user.username,
        "msg": "User created successfully"
    }


@user_router.get("/users/me")
def read_current_user(current_user: Annotated[User, Depends(get_current_user)]) -> UserVM:
    '''
    Route for getting the current user

    Attributes:
        current_user (User): Current User

    Returns:
        User: Current User
    '''
    return current_user
