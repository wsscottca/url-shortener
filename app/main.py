import logging
from fastapi import FastAPI
from api.router.api import api_router
from api.router.auth import auth_router
from api.router.user import user_router
from tests.perform_tests import perform_tests

app = FastAPI()

app.include_router(api_router)
app.include_router(auth_router)
app.include_router(user_router)

logging.getLogger('passlib').setLevel(logging.ERROR)

perform_tests(app)