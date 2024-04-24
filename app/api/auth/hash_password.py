''' Module provides a hash password function used for safe storage in db '''

from app.api.auth.dependencies import password_context

def hash_password(password: str) -> str:
    '''
    Hashes a user's password

    Args:
    password (str): Password to hash

    Returns:
    str: Hashed password
    '''
    return password_context.hash(password)
