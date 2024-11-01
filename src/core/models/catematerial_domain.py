from pydantic import BaseModel
from typing import Optional


class CateMaterialDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    medida: str
