from typing import Dict, TypedDict
from pydantic import BaseModel
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Url_Pair(Model):
    class Meta:
        table_name = 'url'
    
    short_url = UnicodeAttribute(hash_key=True)
    url = UnicodeAttribute()

class Url_Pair_VM(BaseModel):
    short_url: str
    url: str