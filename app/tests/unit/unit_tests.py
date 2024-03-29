from tests.unit.api.list_urls import test_list_url_pairs_empty, test_list_url_pairs_populated
from tests.unit.api.redirect import test_get_redirect_url_does_not_exist, test_get_redirect_url_exists
from tests.unit.api.shorten_url import test_generate_short_url_collision, test_generate_short_url_unique, test_validate_short_url_collision, test_validate_short_url_unique
from tests.unit.db.create_table import test_empty_database
from tests.unit.db.update_item import test_add_url_pair

def unit_tests():
    test_validate_short_url_unique()
    test_validate_short_url_collision()
    test_generate_short_url_unique()
    test_generate_short_url_collision()

    test_get_redirect_url_exists()
    test_get_redirect_url_does_not_exist()

    test_list_url_pairs_empty()
    test_list_url_pairs_populated()

    test_empty_database()
    test_add_url_pair()