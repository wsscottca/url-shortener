from uuid import uuid4
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from pydantic import HttpUrl
from pydantic_settings import BaseSettings
from db.create_table import Url_Pair
import exceptions

class Settings(BaseSettings):
    SERVER_HOST: str

settings = Settings(SERVER_HOST="https://127.0.0.1:8000/")

app = FastAPI()

if not Url_Pair.exists():
    Url_Pair.create_table(wait=True, read_capacity_units=5, write_capacity_units=5)

@app.get("/")
def root():
    return {"message": "URL Shortener API"}

@app.post("/shorten_url", status_code=201)
def shorten_url(url: HttpUrl, short_url: str = None):
    # Check if the user entered short_url causes a collision
    if short_url:
        try:
            Url_Pair.get(short_url)
        except Url_Pair.DoesNotExist:
            pass
        else:
            raise exceptions.KeyExistsError(422, "Short URL already exists, please enter a new short URL.")

    ''' TODO: Swap from truncated uuid to shortuid library'''
    # Truncate uuid
    ''' TODO: validate generated short_url does not already exist in db'''
    short_url = str(uuid4())[:8]

    # Add url pair to db
    url_pair = Url_Pair(short_url, url=str(url))
    url_pair.save()

    # Return JSON response of generated short_url and original url
    return {
        "short_url": f"{settings.SERVER_HOST}" + short_url,
        "url": str(url)
        }

@app.get("/list_urls")
def list_urls():
    url_pairs = {}
    for url_pair in Url_Pair.scan():
        url_pairs[url_pair.short_url] = url_pair.url
    
    return url_pairs

@app.get("/{short_url}")
def redirect(short_url: str):
    # Get original URL if short_url in DB otherwise throw KeyError
    try:
        url_pair = Url_Pair.get(short_url)
        url = url_pair.url
    except Url_Pair.DoesNotExist:
        raise exceptions.KeyError(422, "Short url does not exist.")

    # If there was not a KeyError redirect the user to original URL
    return RedirectResponse(url)