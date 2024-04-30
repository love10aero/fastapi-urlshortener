# Esquemas Pydantic para validación de datos
from pydantic import BaseModel, HttpUrl

class ShortURLBase(BaseModel):
    url: HttpUrl

class ShortURLCreate(ShortURLBase):
    short_code: str

class ShortURLUpdate(ShortURLBase):
    pass
