from abc import ABC, abstractmethod
from src.core.models.material_domain import MaterialDomain


class IMaterialRepository(ABC):

    @abstractmethod
    async def get_all_by_tipo(self, id_tipo: int) -> list[MaterialDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, id_material: int) -> MaterialDomain:
        pass

    @abstractmethod
    async def create(self, mat: MaterialDomain) -> int:
        pass

    @abstractmethod
    async def update(self, id_material: int, mat: MaterialDomain):
        pass

    @abstractmethod
    async def delete(self, id_material: int) -> bool:
        pass
