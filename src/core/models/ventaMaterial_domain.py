from pydantic import BaseModel
from typing import Optional
from src.core.models.material_domain import MaterialDomain
from src.core.models.venta_domain import VentaDomain


class VentaMaterialDomain(BaseModel):
    idVenta: Optional[int] = None
    idMaterial: Optional[int] = None
    Material: Optional[MaterialDomain] = None
    Venta: Optional[VentaDomain] =  None
