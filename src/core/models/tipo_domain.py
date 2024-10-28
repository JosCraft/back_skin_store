from pydantic import BaseModel
from typing import Optional
from src.core.models.color_domain import ColorDomain
from src.core.models.curtiembre_domain import CurtiembreDomain


class TipoDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    medida: str
    idColor: int
    idCurtiembre: int
    color: Optional[ColorDomain] = None
    curtiembre: Optional[CurtiembreDomain] = None
