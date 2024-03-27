from pydantic import BaseModel

class User_VM(BaseModel):
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