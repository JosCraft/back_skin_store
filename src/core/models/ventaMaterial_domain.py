from pydantic import BaseModel
from typing import Optional


class VentaMaterialDomain(BaseModel):
    id: Optional[int] = None
    idMaterial: Optional[int] = None
