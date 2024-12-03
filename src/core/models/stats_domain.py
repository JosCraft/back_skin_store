from pydantic import BaseModel
from typing import Optional


class StatsDomain(BaseModel):
    cant_users: int
    cant_material: int
    cant_ganancias: float
    cant_ventas: int
    
