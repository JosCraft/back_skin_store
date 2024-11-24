from pydantic import BaseModel
from typing import Optional


class UsuarioDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    apelldio: str
    numero: str
    email: str
    password: str
    activo: bool
    role: str
