from fastapi import HTTPException

class KeyExistsError(HTTPException):
    '''Exception for when a short URL already exists in the DB
    
    Used for POST Requests to inform the client that their
    custom short url is already in use so cannot be used
    '''
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

class KeyError(HTTPException):
    ''' Exception for when a short URL does not exist in the DB

    Used for GET Requests to inform the client that the short url
    is not in the DB so a Url_Pair cannot be retrieved
    '''
    def __init__(self, status_code: int, detail: any):
        self.status_code = status_code
        self.detail = detail