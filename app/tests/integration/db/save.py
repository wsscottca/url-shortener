''' Module tests failure in DB dependency save '''

from unittest.mock import patch
from pynamodb.exceptions import PutError
import pytest
from app.db.models.url_pair import UrlPair

@patch('pynamodb.models.Model.save')
def test_db_save_failure(mock_save):
    ''' Test the error is raised when PynamoDB fails a save '''
    mock_save.side_effect = PutError("Failed to save pair to Url_Pair table")
    with pytest.raises(PutError):
        UrlPair().save()
