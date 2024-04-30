from fastapi import FastAPI, HTTPException, status

from app import schemas
from .crud import get_all, get_shorturl, create_shorturl, update_shorturl, partial_update_shorturl, delete_shorturl
# from .dependencies import get_query_token

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint.

    Returns:
        Hello World message.
    """
    return {"message": "Hello World"}

@app.get("/get-all")
async def get_all_shorturl():
    """
    Retrieves all short URLs from the database.

    Returns:
        A list of ShortURL objects representing all the short URLs in the database.
    """
    return get_all()

@app.get("/shorturl/{short_code}")
async def get(short_code: str):
    """
    Get a short URL by its short code.

    Args:
        short_code (str): The short code of the short URL.

    Returns:
        The short URL corresponding to the given short code.

    Raises:
        HTTPException: If the short URL with the given short code does not exist.
    """
    return get_shorturl(short_code)

@app.post("/shorturl/", status_code=status.HTTP_201_CREATED)
async def create(shorturl: schemas.ShortURLCreate):
    """
    Creates a new short URL.

    Args:
        shorturl (schemas.ShortURLCreate): The data for creating the short URL.

    Returns:
        The created short URL.

    Raises:
        HTTPException: If there is an error creating the short URL.

    Note:
        This function is an HTTP POST endpoint that creates a new short URL. It expects a JSON payload with the
        data for creating the short URL. The returned value is the created short URL.

    Example:
        POST /shorturl/
        {
            "short_code": "abc123",
            "url": "https://example.com"
        }
    """
    return create_shorturl(shorturl)

@app.put("/shorturl/{short_code}")
async def update(short_code: str, shorturl: schemas.ShortURLUpdate):
    """
    Update a short URL based on the provided short code and updated data.

    Args:
        short_code (str): The short code of the URL to be updated.
        shorturl (schemas.ShortURLUpdate): The updated data for the short URL.

    Returns:
        The updated short URL.
    """
    return update_shorturl(short_code, shorturl)

@app.patch("/shorturl/{short_code}")
async def partial_update(short_code: str, shorturl: schemas.ShortURLUpdate):
    """
    Patch method to partially update a short URL.

    Args:
        short_code (str): The short code of the URL to be updated.
        shorturl (schemas.ShortURLUpdate): The updated data for the short URL.

    Returns:
        The updated short URL.
    """
    return partial_update_shorturl(short_code, shorturl)

@app.delete("/shorturl/{short_code}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(short_code: str):
    """
    Deletes a short URL from the database.

    Parameters:
        short_code (str): The short code of the URL to be deleted.

    Returns:
        None
    """
    return delete_shorturl(short_code)
