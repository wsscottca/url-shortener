''' Unit tests for list_urls with an empty database '''
from moto import mock_aws
from app.db.services.create_tables import create_table
from app.db.models.url_pair import UrlPair

@mock_aws
def test_empty_database():
    ''' Test our list_urls with an empty database '''
    # Setup
    create_table(UrlPair)

    # Use the client to check if the table is empty
    response = UrlPair.scan()
    assert sum(1 for _ in response) == 0
