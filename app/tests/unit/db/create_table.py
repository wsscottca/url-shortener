from moto import mock_aws
from db.create_tables import create_table
from models.url_pair import Url_Pair

@mock_aws
def test_empty_database():
    # Setup
    create_table(Url_Pair)

    # Use the client to check if the table is empty
    response = Url_Pair.scan()
    assert sum(1 for _ in response) == 0