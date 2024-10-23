from src.core.abstractions.infrastructure.repository.tipo_repository_abstract import ITipoRepository
from src.core.abstractions.services.tipo_service_abstract import ITipoService
from src.core.models.tipo_domain import TipoDomain

class tipoService(ITipoService):

    def __init__(self, tipo_repository: ITipoRepository):
            self.tipo_repository = tipo_repository

    async def get_all_tipo(self):
        return self.tipo_repository.get_all_tipo()

    async def get_tipo_by_id(self, id: int):
        return self.tipo_repository.get_tipo_by_id(id)

    async def create_tipo(self, tipo: TipoDomain):
        return self.tipo_repository.create_tipo(tipo)

    async def update_tipo(self, id: int, tipo: TipoDomain):
        return self.tipo_repository.update_tipo(id, tipo)

    async def delete_tipo(self, id: int):
        return self.tipo_repository.delete_tipo(id)