# external
from pydantic import BaseModel

class Query(BaseModel):
    msg: str

class Response(BaseModel):
    msg: str
