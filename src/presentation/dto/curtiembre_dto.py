from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class CurtiembreDTO(BaseModel):
    id: Optional[int]
    nombre: str
    numero: str
