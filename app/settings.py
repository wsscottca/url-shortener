from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERVER_HOST: str

settings = Settings(SERVER_HOST="https://127.0.0.1:8000/")