from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel

@dataclass
class UsuarioDTO(BaseModel):
    id: Optional[int]
    nombre: str
    apelldio: str
    numero: str
    email: str
    password: str
    activo: bool
    role: str