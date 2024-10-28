from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class InventarioDTO(BaseModel):
    idInventario: Optional[int]
    idMaterial: Optional[int]
