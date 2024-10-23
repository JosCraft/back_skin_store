from pydantic import BaseModel
from typing import Optional


class ColorDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    codigoHex: str