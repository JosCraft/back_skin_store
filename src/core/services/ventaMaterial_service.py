from src.core.abstractions.infrastructure.repository.ventaMaterial_repository_abstract import IVentaMaterialRepository
from src.core.abstractions.services.ventaMaterial_service_abstract import IVentaMaterialService
from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.core.models.material_domain import MaterialDomain


class ventamaterialService(IVentaMaterialService):

    def __init__(self, ventamaterial_repository: IVentaMaterialRepository):
        self.ventamaterial_repository = ventamaterial_repository

    async def get_all_ventamaterial(self) -> list[MaterialDomain]:
        return await self.ventamaterial_repository.get_all()

    async def get_ventamaterial_by_id(self, ventamaterial_id: int) -> MaterialDomain:
        return await self.ventamaterial_repository.get_by_id(ventamaterial_id)

    async def add_ventamaterial(self, ventamaterial: VentaMaterialDomain):
        return await self.ventamaterial_repository.add(ventamaterial)

    async def remove_ventamaterial(self, ventamaterial_id: int) -> bool:
        return await self.ventamaterial_repository.remove(ventamaterial_id)

