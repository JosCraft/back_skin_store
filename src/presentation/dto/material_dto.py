from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class MaterialDTO(BaseModel):
    id: Optional[int]
    medida: str
    idTipo: Optional[int]
