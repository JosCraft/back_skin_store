from pydantic import BaseModel
from typing import Optional


class CurtiembreDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    numero: str
