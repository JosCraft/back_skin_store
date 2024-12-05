from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel

@dataclass
class UsuarioDTO(BaseModel):
    id: Optional[int]
    nombre: Optional[str]
    apelldio: Optional[str]
    numero: Optional[str]
    email: Optional[str]
    password: Optional[str]
    activo: Optional[bool]
    role: Optional[str]