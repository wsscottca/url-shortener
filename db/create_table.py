from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Url_Pair(Model):
    class Meta:
        table_name = 'url'
    
    short_url = UnicodeAttribute(hash_key=True)
    url = UnicodeAttribute()