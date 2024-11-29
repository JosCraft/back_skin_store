from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel
from datetime import date


@dataclass
class VentaDTO(BaseModel):
    id: Optional[int]
    fecha: date
    totalVenta: str
    idUsuario: Optional[int]
