from abc import ABC, abstractmethod
from src.core.models.venta_domain import VentaDomain


class IVentaRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[VentaDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, id_sale: int) -> VentaDomain:
        pass

    @abstractmethod
    async def create(self, ven: VentaDomain):
        pass

    @abstractmethod
    async def update(self, id_sale: int, ven: VentaDomain):
        pass

    @abstractmethod
    async def delete(self, id_sale: int) -> bool:
        pass
