from pydantic import BaseModel

class PersonIn(BaseModel):
    name: str
    npm: int

class PersonOut(PersonIn):
    id: int