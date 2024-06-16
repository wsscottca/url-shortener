''' Module contains the UrlPairVM used by the routes for proper SwaggerUI docs '''

from typing import Annotated
from fastapi import Query
from pydantic import BaseModel

class UrlPairVM(BaseModel):
    '''
    Url Pair View Model 
    extends pydantic BaseModel for SwaggerUI docs
    
    Attributes:
        short_url (str): short url used as key
        url (str): original url string to redirect to when short url is accessed
    '''
    short_url: str
    url: str

ShortUrl = Annotated[str, Query(max_length=8)]
