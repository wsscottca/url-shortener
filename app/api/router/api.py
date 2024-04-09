import logging
from typing import Annotated, Dict

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl

from api.exceptions import CredentialError
from api.models.url_pair import Url_Pair_VM
from api.generate_short_url import generate_short_url, validate_url_unique
from api.user.get_current_user import get_current_user
from api.user.validate_permissions import validate_user_permissions
from db.models.url_pair import Url_Pair
from db.services.list_urls import get_urls
from db.services.redirect import get_redirect_url
from settings import settings
from api.auth.dependencies import oauth2_scheme

api_router = APIRouter()

@api_router.get("/")
def root():
    return {"message": "URL Shortener API"}

@api_router.post("/shorten_url", status_code=201, response_model=Url_Pair_VM)
def shorten_url(url: HttpUrl, short_url: str = None) -> Dict[str, str]:
    if not short_url:
        short_url = generate_short_url()
    else:
        validate_url_unique(short_url)
        
    new_pair = Url_Pair(short_url, url=str(url))
    new_pair.save()

    return {
        "short_url": f"{settings.SERVER_HOST}" + short_url,
        "url": str(url)
        }

@api_router.get("/list_urls")
def list_urls(token: Annotated[str, Depends(oauth2_scheme)]) -> Dict[int, Url_Pair_VM]:
    user = get_current_user(token)
    validate_user_permissions(user, "admin")

    url_pairs = get_urls()
    return url_pairs

@api_router.get("/{short_url}", status_code=307)
def redirect(short_url: str) -> RedirectResponse:
    url = get_redirect_url(short_url)
    return RedirectResponse(url)

