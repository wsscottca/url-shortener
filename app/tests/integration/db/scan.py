''' Module tests failure in DB dependency scan '''

from unittest.mock import patch
from pynamodb.exceptions import ScanError
import pytest
from app.db.models.url_pair import UrlPair

@patch('pynamodb.models.Model.scan')
def test_db_scan_failure(mock_scan):
    ''' Test the error is raised when PynamoDB fails a scan '''
    mock_scan.side_effect = ScanError("Failed to scan Url_Pair table")
    with pytest.raises(ScanError):
        UrlPair.scan()
