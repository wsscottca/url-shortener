from typing import Dict
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl
from pydantic_settings import BaseSettings
from api.list_urls import get_urls
from api.redirect import get_redirect_url
from api.shorten_url import validate_short_url
from tests.perform_tests import perform_tests
from db.update_item import update_item
from models.url_pair import Url_Pair, Url_Pair_VM

class Settings(BaseSettings):
    SERVER_HOST: str

settings = Settings(SERVER_HOST="https://127.0.0.1:8000/")
app = FastAPI()

@app.get("/")
def root():
    return {"message": "URL Shortener API"}

@app.post("/shorten_url", status_code=201, response_model=Url_Pair_VM)
def shorten_url(url: HttpUrl, short_url: str = None):
    short_url = validate_short_url(short_url)
    update_item(Url_Pair(short_url, url=str(url)))

    return {
        "short_url": f"{settings.SERVER_HOST}" + short_url,
        "url": str(url)
        }

@app.get("/list_urls")
def list_urls() -> Dict[int, Url_Pair_VM]:
    url_pairs = get_urls()
    return url_pairs

@app.get("/{short_url}", status_code=307)
def redirect(short_url: str):
    url = get_redirect_url(short_url)
    return RedirectResponse(url)

perform_tests(app)