from pydantic import BaseModel

class Url_Pair_VM(BaseModel):
    '''
    Url Pair View Model extends pydantic BaseModel for SwaggerUI docs to have contextual information about the Url pair 
    
    Attributes:
        short_url (str): short url used as key
        url (str): original url string to redirect to when short url is accessed
    '''
    short_url: str
    url: str