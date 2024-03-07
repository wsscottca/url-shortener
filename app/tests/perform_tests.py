from fastapi.testclient import TestClient
from tests.list_urls import test_list_urls, test_list_urls_empty
from tests.redirect import test_bad_redirect, test_redirect
from tests.root import test_get_root
from tests.shorten_url import clear_url, test_generate_url, test_shorten_url_invalid, test_shorten_url_valid, test_validate_url, test_validate_url_invalid

def perform_tests(app):
    client = TestClient(app)
    test_get_root(client)

    test_redirect(client)
    test_bad_redirect(client)
    test_list_urls(client)
    # test_list_urls_empty(client)

    test_generate_url()
    test_validate_url()
    test_validate_url_invalid()
    test_shorten_url_valid(client)
    test_shorten_url_invalid(client)
    # Remove test entry short_url
    clear_url()