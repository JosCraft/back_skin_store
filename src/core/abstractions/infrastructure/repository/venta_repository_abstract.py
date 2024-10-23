from abc import ABC, abstractmethod
from src.core.models.venta_domain import VentaDomain


class IVentaRepository(ABC):

        @abstractmethod
        def get_all(self) -> list[VentaDomain]:
            pass

        @abstractmethod
        def get_by_id(self, id_sale: int) -> VentaDomain:
            pass

        @abstractmethod
        def create(self, ven: VentaDomain):
            pass

        @abstractmethod
        def update(self, id_sale: int, ven: VentaDomain):
            pass

        @abstractmethod
        def delete(self, id_sale: int) -> bool:
            pass
