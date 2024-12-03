from pydantic import BaseModel
from typing import Optional
from datetime import date
from src.core.models.usuario_domain import UsuarioDomain

class VentaDomain(BaseModel):
    id: Optional[int] = None
    fecha: date
    totalVenta: str
    idUsuario: Optional[int] = None
    usuario: Optional[UsuarioDomain] = None
