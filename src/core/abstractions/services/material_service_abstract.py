from abc import ABC, abstractmethod
from src.core.models.material_domain import MaterialDomain


class IMaterialService(ABC):
    @abstractmethod
    async def get_all_material(self) -> list[MaterialDomain]:
        pass

    @abstractmethod
    async def get_material_by_id(self, material_id: int) -> MaterialDomain:
        pass

    @abstractmethod
    async def create_material(self, material_id: int, material: MaterialDomain):
        pass

    @abstractmethod
    async def update_material(self, material_id: int, material: MaterialDomain):
        pass

    @abstractmethod
    async def delete_material(self, material_id: int) -> bool:
        pass