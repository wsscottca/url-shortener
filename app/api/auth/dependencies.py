import os
from dotenv import find_dotenv, load_dotenv
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

load_dotenv(find_dotenv(), override=True)

ALGORITHM = "HS256"
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

