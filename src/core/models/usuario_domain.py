from pydantic import BaseModel
from typing import Optional


class UsuarioDomain(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    apelldio: Optional[str] = None
    numero: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    activo: Optional[bool] = None
    role: Optional[str] = None
