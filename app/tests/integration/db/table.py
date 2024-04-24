''' Module tests failure in DB dependency creating a table '''

from unittest.mock import patch
from pynamodb.exceptions import TableError
import pytest
from app.db.models.url_pair import UrlPair

@patch('pynamodb.models.Model.create_table')
def test_db_create_table_failure(mock_create_table):
    ''' Test the error is raised when PynamoDB fails a table creation '''
    mock_create_table.side_effect = TableError("Failed to create Url_Pair table")
    with pytest.raises(TableError):
        UrlPair.create_table()
