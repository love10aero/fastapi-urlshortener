# Lógica de operaciones CRUD (si aplica)
from fastapi import HTTPException
from .models import db

def get_all():
    print(db)
    print("**********)")
    return db

def get_shorturl(short_code: str):
    if short_code in db:
        return db[short_code]
    raise HTTPException(status_code=404, detail="ShortURL not found")

def create_shorturl(shorturl):
    db[shorturl.short_code] = shorturl
    return shorturl

def update_shorturl(short_code: str, shorturl):
    db[short_code] = shorturl
    return shorturl

def partial_update_shorturl(short_code: str, shorturl):
    stored_shorturl_model = db[short_code]
    update_data = shorturl.dict(exclude_unset=True)
    updated_shorturl = stored_shorturl_model.copy(update=update_data)
    db[short_code] = updated_shorturl
    return updated_shorturl

def delete_shorturl(short_code: str):
    del db[short_code]
    return
