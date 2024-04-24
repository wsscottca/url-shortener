''' Module contains API related routes. '''

from typing import Annotated, Dict

from fastapi import APIRouter, Depends, Query, Path
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl

from app.api.models.url_pair import UrlPairVM
from app.api.generate_short_url import generate_short_url, validate_url_unique
from app.api.user.get_current_user import get_current_user
from app.api.user.validate_permissions import validate_user_permissions
from app.db.models.url_pair import UrlPair
from app.db.services.list_urls import get_urls
from app.db.services.redirect import get_redirect_url
from app.settings import settings
from app.api.auth.dependencies import oauth2_scheme

api_router = APIRouter()

@api_router.get("/")
def root():
    ''' Root route, with a simple return message '''
    return {"message": "URL Shortener API"}

@api_router.post("/shorten_url", status_code=201, response_model=UrlPairVM)
def shorten_url(url: HttpUrl,
                short_url: Annotated[str | None, Query(max_length=8)] = None) -> Dict[str, str]:
    '''
    Shorten URL route, creates a short url for a provided valid url,
    if not provided a short url generates one.

    Attributes:
        url (HTTPUrl): Valid web address that we're creating a short_url for
        short_url (str | None): Optional short_url to use - max length 8

    Returns:
        Dict[str, str]: JSONable dict of the url and short_url
    '''
    if not short_url:
        short_url = generate_short_url()
    else:
        validate_url_unique(short_url)

    new_pair = UrlPair(short_url, url=str(url))
    new_pair.save()

    return {
        "short_url": f"{settings.SERVER_HOST}" + short_url,
        "url": str(url)
        }

@api_router.get("/list_urls")
def list_urls(token: Annotated[str, Depends(oauth2_scheme)]) -> Dict[int, UrlPairVM]:
    '''
    List URLs route, requires a user that is correctly authenticated 
    and has the correct permissions

    Attributes:
        token (oauth2_scheme): Password Bearer JWT

    Returns:
        Dict[int, UrlPairVM]: JSONable dict of the count and Url Pair
    '''
    user = get_current_user(token)
    validate_user_permissions(user, "admin")

    url_pairs = get_urls()
    return url_pairs

@api_router.get("/{short_url}", status_code=307)
def redirect(short_url: Annotated[str, Path(max_length=8)]) -> RedirectResponse:
    '''
    Redirect route, when given a short url, reroutes the user to the
    related original url

    Attributes:
        short_url (str): Short URL index - max length 8

    Returns:
        RedirectResponse: Redirects the user to the related original URL
    '''
    url = get_redirect_url(short_url)
    return RedirectResponse(url)

