from abc import ABC, abstractmethod
from src.core.models.material_domain import MaterialDomain
from src.core.models.inventario_domain import InventarioDomain


class IInventarioService(ABC):

    @abstractmethod
    def get_all_inventario(self) -> list[MaterialDomain]:
        pass

    @abstractmethod
    def get_inventario_by_id(self, id_material: int) -> MaterialDomain:
        pass

    @abstractmethod
    def add_inventario(self, inventario: InventarioDomain):
        pass

    @abstractmethod
    def remove_inventario(self, id_material: int) -> bool:
        pass