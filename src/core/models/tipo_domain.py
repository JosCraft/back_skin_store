from pydantic import BaseModel
from typing import Optional
from src.core.models.color_domain import ColorDomain
from src.core.models.curtiembre_domain import CurtiembreDomain


class TipoDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: Optional[float] = None
    idCategoria: Optional[int] = None
    idColor: Optional[int] = None
    idCurtiembre: Optional[int] = None
    color: Optional[ColorDomain] = None
    curtiembre: Optional[CurtiembreDomain] = None
    cantVentas: Optional[int] = None
    ganancias: Optional[float] = None
