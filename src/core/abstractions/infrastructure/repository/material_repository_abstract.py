from abc import ABC, abstractmethod
from src.core.models.material_domain import MaterialDomain


class IMaterialRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[MaterialDomain]:
        pass

    @abstractmethod
    def get_by_id(self, id_material: int) -> MaterialDomain:
        pass

    @abstractmethod
    def create(self, mat: MaterialDomain):
        pass

    @abstractmethod
    def update(self, id_material: int, mat: MaterialDomain):
        pass

    @abstractmethod
    def delete(self, id_material: int) -> bool:
        pass
