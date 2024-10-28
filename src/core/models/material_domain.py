from pydantic import BaseModel
from typing import Optional

from src.core.models.tipo_domain import TipoDomain


class MaterialDomain(BaseModel):
    id: Optional[int] = None
    medida: str
    idTipo: Optional[int] = None
