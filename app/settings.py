''' Module contains settings class for application '''

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ''' Settings that defines server host '''
    SERVER_HOST: str

settings = Settings(SERVER_HOST="https://127.0.0.1:8000/")
