from abc import ABC, abstractmethod
from src.core.models.material_domain import MaterialDomain
from src.core.models.inventario_domain import InventarioDomain


class IInventarioRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[MaterialDomain]:
        pass

    @abstractmethod
    def get_by_id(self, id_material: int) -> MaterialDomain:
        pass

    @abstractmethod
    def add(self, inv: InventarioDomain):
        pass

    @abstractmethod
    def remove(self, id_material: int) -> bool:
        pass
