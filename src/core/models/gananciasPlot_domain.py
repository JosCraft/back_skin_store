from pydantic import BaseModel
from typing import Optional
from datetime import date

class GananciasDomain(BaseModel):
    fecha: date
    ganancia: float