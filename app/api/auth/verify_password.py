''' Module includes verify password function to validate a password against a hash '''

from app.api.auth.dependencies import password_context

def verify_password(password: str, hashed_pass: str) -> bool:
    '''
    Verifys if the hashed password is the hash for the given password

    Args:
    password (str): Password to verify
    hashed_pass (str): Hashed password to validate against

    Returns:
    bool: If the password and hash match
    '''
    return password_context.verify(password, hashed_pass)
