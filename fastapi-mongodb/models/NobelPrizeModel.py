from pydantic import BaseModel

from models.LaureatesModel import Laureates


class NobelPrize(BaseModel):
    year: str
    category: str
    laureates: list[Laureates]
