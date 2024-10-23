from pydantic import BaseModel
from typing import Optional


class InventarioDomain(BaseModel):
    idInventario : Optional[int] = None
    idMaterial : Optional[int] = None
