from abc import ABC, abstractmethod
from src.core.models.venta_domain import VentaDomain

class IVentaService(ABC):
    @abstractmethod
    async def get_all_venta(self) -> list[VentaDomain]:
        pass

    @abstractmethod
    async def get_venta_by_id(self, venta_id: int) -> VentaDomain:
        pass

    @abstractmethod
    async def create_venta(self, venta: VentaDomain):
        pass


    @abstractmethod
    async def delete_venta(self, venta_id: int) -> bool:
        pass
