from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class ColorDTO(BaseModel):
    id: Optional[int]
    nombre: str
    codigo: str
