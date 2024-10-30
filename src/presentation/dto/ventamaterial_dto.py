from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class VentaMaterialDTO(BaseModel):
    idVenta: Optional[int]
    idMaterial: Optional[int]
