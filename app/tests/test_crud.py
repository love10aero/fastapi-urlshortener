from fastapi import HTTPException
import pytest
from app.crud import create_shorturl, get_shorturl
from app.schemas import ShortURLCreate

def test_get_nonexistent_shorturl():
    with pytest.raises(HTTPException):
        get_shorturl("nonexistent")

def test_create_and_get_shorturl():
    shorturl = ShortURLCreate(short_code="testcode", url="https://test.com")
    create_shorturl(shorturl)
    assert get_shorturl("testcode") == shorturl
