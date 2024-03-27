from moto import mock_aws
from db.services.create_tables import create_table
from db.models.url_pair import Url_Pair

@mock_aws
def test_add_url_pair():
    # Setup
    create_table(Url_Pair)
    Url_Pair('1234abcd', url='https://example.com').save()

    # Retrieve item from the mocked DB
    saved_url = Url_Pair.get('1234abcd')
    assert saved_url.url == 'https://example.com'