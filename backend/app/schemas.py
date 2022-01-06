# Pydantic models (schemas) is used when reading data, when returning it from the API
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: str
    website: str

    class Config:
        orm_mode = True