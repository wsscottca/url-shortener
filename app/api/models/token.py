'''  Module contains API models Token and TokenData '''

from pydantic import BaseModel


class Token(BaseModel):
    '''
    Token class defines JWT OAuth2 type and carries the token string
    extends Pydantic BaseModel for proper SwaggerUI documentation

    Attributes:
        access_token (str): Token string
        token_type (str): Type of token
    '''
    access_token: str
    token_type: str

class TokenData(BaseModel):
    '''
    Token Data class defines what information is found in a JWT
    extends Pydantic BaseModel for proper SwaggerUI documentation

    Attributes:
        username (str | None): user
    '''
    username: str | None = None
