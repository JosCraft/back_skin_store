from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class CateMaterialDTO(BaseModel):
    id: Optional[int]
    nombre: str
    medida: str
