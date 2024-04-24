''' Module contains UrlPair DB model. '''

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class UrlPair(Model):
    '''
    Url Pair extends pynamodb Model class, defines url table and columns
    
    Attributes:
        short_url (UnicodeAttribute): short url string - hash key for table in db
        url (UnicodeAttribute): original url string to redirect to when short url is accessed
    '''
    class Meta:
        ''' Metadata for DB '''
        region = 'us-west-1'
        table_name = 'url'

    short_url = UnicodeAttribute(hash_key=True)
    url = UnicodeAttribute()
