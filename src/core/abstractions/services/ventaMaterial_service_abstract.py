from abc import ABC, abstractmethod
from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.core.models.material_domain import MaterialDomain


class IVentaMaterialService(ABC):

    @abstractmethod
    async def get_all_ventamaterial(self) -> list[MaterialDomain]:
        pass

    @abstractmethod
    async def get_ventamaterial_by_id(self, ventaMaterial_id: int) -> MaterialDomain:
        pass

    @abstractmethod
    async def create_ventamaterial(self, ventaMaterial: VentaMaterialDomain):
        pass

    @abstractmethod
    async def update_ventamaterial(self, ventaMaterial_id: int, ventaMaterial: VentaMaterialDomain):
        pass

    @abstractmethod
    async def delete_ventamaterial(self, ventaMaterial_id: int) -> bool:
        pass
