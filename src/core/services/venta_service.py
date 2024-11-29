from src.core.abstractions.infrastructure.repository.venta_repository_abstract import IVentaRepository
from src.core.abstractions.services.venta_service_abstract import IVentaService
from src.core.models.venta_domain import VentaDomain


class ventaService(IVentaService):
    def __init__(self, venta_repository: IVentaRepository):
        self.venta_repository = venta_repository

    async def get_all_venta(self) -> list[VentaDomain]:
        return await self.venta_repository.get_all()

    async def get_venta_by_id(self, venta_id: int) -> VentaDomain:
        return await self.venta_repository.get_by_id(venta_id)

    async def create_venta(self, venta: VentaDomain) -> int:
        return await self.venta_repository.create(venta)
