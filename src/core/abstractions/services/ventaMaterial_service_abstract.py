from abc import ABC, abstractmethod
from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.core.models.material_domain import MaterialDomain


class IVentaMaterialService(ABC):

    @abstractmethod
    async def get_all_ventamaterial(self) -> list[MaterialDomain]:
        pass

    @abstractmethod
    async def get_ventamaterial_by_id(self, ventamaterial_id: int) -> MaterialDomain:
        pass

    @abstractmethod
    async def add_ventamaterial(self, ventamaterial: VentaMaterialDomain):
        pass

    @abstractmethod
    async def remove_ventamaterial(self, ventamaterial_id: int) -> bool:
        pass
