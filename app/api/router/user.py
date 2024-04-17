from typing import Annotated

from fastapi import APIRouter, Depends, Form, Query
from api.auth.hash_password import hash_password
from api.models.user import User_VM
from api.user.get_current_user import get_current_user
from db.models.user import User
from db.services.validate_username_unique import validate_user_unique

user_router = APIRouter()

@user_router.post("/signup", status_code=201)
def create_user(username: Annotated[str, Query(max_length=16, min_length=4), Form()], password: Annotated[str, Query(max_length=32, min_length=8), Form()]):
    hashed_password = hash_password(password)
    username = validate_user_unique(username)
    new_user = User(username, password=hashed_password, group="user", disabled=False)
    new_user.save()
    return {
        "username": new_user.username,
        "msg": "User created successfully"
    }


@user_router.get("/users/me")
def read_current_user(current_user: Annotated[User, Depends(get_current_user)]) -> User_VM:
    return current_user