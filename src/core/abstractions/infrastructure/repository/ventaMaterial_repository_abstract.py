from abc import ABC, abstractmethod
from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.core.models.material_domain import MaterialDomain


class IVentaMaterialRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[MaterialDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, id_material: int) -> MaterialDomain:
        pass

    @abstractmethod
    async def add(self, ven: VentaMaterialDomain):
        pass

    @abstractmethod
    async def remove(self, id_material: int) -> bool:
        pass
