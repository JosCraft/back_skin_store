from src.core.abstractions.infrastructure.repository.ventaMaterial_repository_abstract import IVentaMaterialRepository
from src.core.abstractions.services.ventaMaterial_service_abstract import IVentaMaterialService
from src.core.models.ventaMaterial_domain import VentaMaterialDomain

class ventaMaterialService(IVentaMaterialService):

    def __init__(self, ventaMaterial_repository: IVentaMaterialRepository):
        self.ventaMaterial_repository = ventaMaterial_repository

    async def create(self, ventaMaterial: VentaMaterialDomain):
        return await self.ventaMaterial_repository.create(ventaMaterial)

    async def get(self, id: int):
        return await self.ventaMaterial_repository.get(id)

    async def get_all(self):
        return await self.ventaMaterial_repository.get_all()

    async def update(self, ventaMaterial: VentaMaterialDomain):
        return await self.ventaMaterial_repository.update(ventaMaterial)

    async def delete(self, id: int):
        return await self.ventaMaterial_repository.delete(id)
