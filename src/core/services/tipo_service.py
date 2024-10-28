from src.core.abstractions.infrastructure.repository.tipo_repository_abstract import ITipoRepository
from src.core.abstractions.services.tipo_service_abstract import ITipoService
from src.core.models.tipo_domain import TipoDomain


class tipoService(ITipoService):

    def __init__(self, tipo_repository: ITipoRepository):
        self.tipo_repository = tipo_repository

    async def get_all_tipo(self) -> list[TipoDomain]:
        return await self.tipo_repository.get_all()

    async def get_tipo_by_id(self, tipo_id: int) -> TipoDomain:
        return await self.tipo_repository.get_by_id(tipo_id)

    async def create_tipo(self, tipo: TipoDomain):
        return await self.tipo_repository.create(tipo)

    async def update_tipo(self, tipo_id: int, tipo: TipoDomain):
        return await self.tipo_repository.update(tipo_id, tipo)

    async def delete_tipo(self, tipo_id: int):
        return await self.tipo_repository.delete(tipo_id)
