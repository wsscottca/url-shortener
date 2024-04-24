''' Update item unit tests '''
from moto import mock_aws
from app.db.services.create_tables import create_table
from app.db.models.url_pair import UrlPair

@mock_aws
def test_add_url_pair():
    ''' Test adding a url pair to ensure adding to our DB is funcitoning '''
    # Setup
    create_table(UrlPair)
    UrlPair('1234abcd', url='https://example.com').save()

    # Retrieve item from the mocked DB
    saved_url = UrlPair.get('1234abcd')
    assert saved_url.url == 'https://example.com'
