from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class TipoDTO(BaseModel):
    id: Optional[int]
    nombre: str
    precio: float
    medida: str
    idColor: int
    idCurtiembre: int
