from pydantic import BaseModel
from typing import Optional


class TipoDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    idColor: int
    idCurtiembre: int