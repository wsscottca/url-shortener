''' Module contains User DB model '''

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute

class User(Model):
    '''
    User extends pynamodb Model class, defines user table and columns
    
    Attributes:
        username (UnicodeAttribute): user's username - hash key for table in db
        password (UnicodeAttribute): hashed passsword
        group (UnicodeAttribute): user's privilege group
        disabled (BooleanAttribute): user's account status
    '''
    class Meta:
        ''' Metadata for DB '''
        region = 'us-west-1'
        table_name = 'user'

    username = UnicodeAttribute(hash_key=True)
    password = UnicodeAttribute()
    group = UnicodeAttribute()
    disabled = BooleanAttribute()
