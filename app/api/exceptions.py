''' Module contains all exceptions used by the API '''

from fastapi import HTTPException

class KeyExistsError(HTTPException):
    '''
    Exception for when an item already exists in the DB
    
    Used for POST Requests to inform the client that their
    key is already in use so cannot be used

    Attributes:
        status_code (int): HTTP Status Code
        detail (str): Message to be sent to the client detailing the error
    '''
    def __init__(self, status_code: int, detail: any):
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code, detail)

class KeyDoesNotExistError(HTTPException):
    '''
    Exception for when an item does not exist in the DB

    Used for GET Requests to inform the client that the key
    is not in the DB so an item cannot be retrieved

    Attributes:
        status_code (int): HTTP Status Code
        detail (str): Message to be sent to the client detailing the error
    '''
    def __init__(self, status_code: int, detail: any):
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code, detail)

class CredentialError(HTTPException):
    '''
    Exception for when there is an error authenticating a user

    Attributes:
        status_code (int): HTTP Status Code
        detail (str): Message to be sent to the client detailing the error
    '''
    def __init__(self, status_code: int, detail: any):
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code, detail)

class InputError(HTTPException):
    '''
    Exception for when there is an unprocessable input.

    Attributes:
        status_code (int): HTTP Status Code
        detail (str): Message to be sent to the client detailing the error
    '''
    def __init__(self, detail: any, status_code: int = 422):
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code, detail)
