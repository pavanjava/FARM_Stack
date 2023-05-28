from pydantic import BaseModel


class Laureates(BaseModel):
    firstname: str
    surname: str
    motivation: str
    share: str

