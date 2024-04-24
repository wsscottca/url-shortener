''' All unit tests related to the API '''
from app.tests.unit.api.list_urls import test_list_url_pairs_empty, test_list_url_pairs_populated
from app.tests.unit.api.redirect import (test_get_redirect_url_does_not_exist,
    test_get_redirect_url_exists)
from app.tests.unit.api.shorten_url import (test_generate_short_url_collision,
    test_generate_short_url_unique, test_validate_short_url_collision,
    test_validate_short_url_unique)


def api_unit_tests():
    ''' API Unit tests '''
    #pylint: disable=no-value-for-parameter
    test_validate_short_url_unique()
    test_validate_short_url_collision()
    test_generate_short_url_unique()
    test_generate_short_url_collision()

    test_get_redirect_url_exists()
    test_get_redirect_url_does_not_exist()

    test_list_url_pairs_empty()
    test_list_url_pairs_populated()
    #pylint: enable=no-value-for-parameter
