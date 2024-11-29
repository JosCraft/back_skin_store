from pydantic import BaseModel
from typing import Optional
from datetime import date


class VentaDomain(BaseModel):
    id: Optional[int] = None
    fecha: date
    totalVenta: str
    idUsuario: Optional[int] = None
