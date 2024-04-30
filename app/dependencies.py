# Dependencias, funciones de ayuda, y componentes
from fastapi import Header, HTTPException

async def get_query_token(x_token: str = Header(...)):
    if x_token != "supersecrettoken":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token
