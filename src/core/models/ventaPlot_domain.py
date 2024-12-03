from pydantic import BaseModel
from typing import Optional

class ventaPlotDomain(BaseModel):
    tipoMaterial: str
    totalVentas: int
    totalIngresos: float