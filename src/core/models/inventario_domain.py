from pydantic import BaseModel
from typing import Optional
from src.core.models.material_domain import MaterialDomain


class InventarioDomain(BaseModel):
    idInventario: Optional[int] = None
    idMaterial: Optional[int] = None
    material: Optional[MaterialDomain] = None
