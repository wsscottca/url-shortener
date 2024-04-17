from tests.integration.api.list_urls import test_list_urls, test_list_urls_expired_token
from tests.integration.api.redirect import test_bad_redirect, test_bad_redirect_long, test_redirect
from tests.integration.api.root import test_get_root
from tests.integration.api.shorten_url import clear_url, test_generate_url, test_shorten_url_invalid, test_shorten_url_invalid_short_url, test_shorten_url_invalid_url, test_shorten_url_valid, test_validate_url, test_validate_url_invalid

def api_integration_tests(client):
    clear_url()
    test_get_root(client)

    test_redirect(client)
    test_bad_redirect(client)
    test_bad_redirect_long(client)
    
    test_list_urls(client)
    test_list_urls_expired_token(client)

    test_generate_url()
    test_validate_url()
    test_validate_url_invalid()
    test_shorten_url_valid(client)
    test_shorten_url_invalid(client)
    test_shorten_url_invalid_short_url(client)
    test_shorten_url_invalid_url(client)

    # Remove test entry short_url
    clear_url()