''' Module tests failure in DB dependency get '''

from unittest.mock import patch
from pynamodb.exceptions import GetError
import pytest
from app.db.models.url_pair import UrlPair

@patch('pynamodb.models.Model.get')
def test_db_get_failure(mock_get):
    ''' Test the error is raised when PynamoDB fails a get '''
    mock_get.side_effect = GetError("Failed to get pair from URL table")
    with pytest.raises(GetError):
        UrlPair().get("key")
