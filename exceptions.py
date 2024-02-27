from fastapi import HTTPException

class KeyExistsError(HTTPException):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

class KeyError(HTTPException):
    def __init__(self, status_code: int, detail: any):
        self.status_code = status_code
        self.detail = detail