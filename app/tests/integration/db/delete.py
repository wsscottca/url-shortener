''' Module tests failure in DB dependency deletion '''

from unittest.mock import patch
from pynamodb.exceptions import DeleteError
import pytest
from app.db.models.url_pair import UrlPair

@patch('pynamodb.models.Model.delete')
def test_db_delete_failure(mock_delete):
    ''' Test the error is raised when PynamoDB fails a deletion '''
    mock_delete.side_effect = DeleteError("Failed to delete pair")
    with pytest.raises(DeleteError):
        UrlPair().delete()
