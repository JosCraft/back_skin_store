from pydantic import BaseModel
from typing import Optional

from src.core.models.tipo_domain import TipoDomain


class MaterialDomain(BaseModel):
    id: Optional[int] = None
    medida: float
    idTipo: Optional[int] = None
    tipo: Optional[TipoDomain] = None
