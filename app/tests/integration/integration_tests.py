from tests.integration.list_urls import test_list_urls
from tests.integration.redirect import test_bad_redirect, test_redirect
from tests.integration.root import test_get_root
from tests.integration.shorten_url import clear_url, test_generate_url, test_shorten_url_invalid, test_shorten_url_valid, test_validate_url, test_validate_url_invalid

def integration_tests(client):
    clear_url()
    test_get_root(client)

    test_redirect(client)
    test_bad_redirect(client)
    
    # need to modify for users
    #test_list_urls(client)

    test_generate_url()
    test_validate_url()
    test_validate_url_invalid()
    test_shorten_url_valid(client)
    test_shorten_url_invalid(client)

    # Remove test entry short_url
    clear_url()