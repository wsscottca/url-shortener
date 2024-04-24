''' Module tests failure in DB dependency connection '''

from unittest.mock import patch
from pynamodb.exceptions import PynamoDBConnectionError
import pytest
from app.db.models.url_pair import UrlPair

@patch('pynamodb.models.Model.exists')
def test_db_conn_failure(mock_conn):
    ''' Tests a connection failure in the DB dependency '''
    mock_conn.side_effect = PynamoDBConnectionError("Connection Error")
    with pytest.raises(PynamoDBConnectionError):
        if not UrlPair.exists():
            pass
