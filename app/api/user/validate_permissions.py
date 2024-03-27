from api.exceptions import CredentialError
from db.models.user import User


def validate_user_permissions(user: User, group: str) -> bool:
    '''
    Validates the user is in the correct permission group for a given function.
    
    Args:
        user (User): The user whose group we're verifying
        group (str): The group the user needs to be in

    Raises:
        CredentialError: Invalid permissions

    Returns:
        bool: If the validation was successful
    '''
    if user.group != group:
        raise CredentialError(401, "You do not have the appropriate permissions to access this route.")
    
    return True