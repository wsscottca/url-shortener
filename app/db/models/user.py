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
        table_name = 'user'
    
    username = UnicodeAttribute(hash_key=True)
    password = UnicodeAttribute()
    group = UnicodeAttribute()
    disabled = BooleanAttribute()