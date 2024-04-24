''' Module contains the UserVM model used by routes for proper contextual SwaggerUI docs'''

from pydantic import BaseModel

class UserVM(BaseModel):
    '''
    User View Model extends pydantic BaseModel for SwaggerUI docs
    to have contextual information about the User
    
    Attributes:
        username (str): short url used as key
        password (str): hashed password
        group (str): user's privilege group
        disabled (bool): user's account status
    '''
    username: str
    password: str
