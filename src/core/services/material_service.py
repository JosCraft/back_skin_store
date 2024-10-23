from src.core.abstractions.infrastructure.repository.material_repository_abstract import IMaterialRepository
from src.core.abstractions.services.material_service_abstract import IMaterialService
from src.core.models.material_domain import MaterialDomain

class materialService(IMaterialService):

    def __init__(self, material_repository: IMaterialRepository):
        self.material_repository = material_repository

    async def get_all_material(self):
        return self.material_repository.get_all_material()

    async def get_material_by_id(self, id: int):
        return self.material_repository.get_material_by_id(id)

    async def create_material(self, material: MaterialDomain):
        return self.material_repository.create_material(material)

    async def update_material(self, id: int, material: MaterialDomain):
        return self.material_repository.update_material(id, material)

    async def delete_material(self, id: int):
        return self.material_repository.delete_material(id)