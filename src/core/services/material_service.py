from src.core.abstractions.infrastructure.repository.material_repository_abstract import IMaterialRepository
from src.core.abstractions.services.material_service_abstract import IMaterialService
from src.core.models.material_domain import MaterialDomain


class materialService(IMaterialService):

    def __init__(self, material_repository: IMaterialRepository):
        self.material_repository = material_repository

    async def get_all_by_tipo_material(self, id_tipo: int) -> list[MaterialDomain]:
        return await self.material_repository.get_all_by_tipo(id_tipo)

    async def get_material_by_id(self, id_material: int) -> MaterialDomain:
        return await self.material_repository.get_by_id(id_material)

    async def create_material(self, material: MaterialDomain) -> int:
        return await self.material_repository.create(material)

    async def update_material(self, id_material: int, material: MaterialDomain):
        return await self.material_repository.update(id_material, material)

    async def delete_material(self, id_material: int):
        return await self.material_repository.delete(id_material)
