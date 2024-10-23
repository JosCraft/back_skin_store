from src.core.abstractions.infrastructure.repository.inventario_repository_abstract import IInventarioRepository
from src.core.abstractions.services.inventario_service_abstract import IInventarioService
from src.core.models.inventario_domain import InventarioDomain
from src.core.models.material_domain import MaterialDomain


class inventarioService(IInventarioService):

    def __init__(self, inventario_repository: IInventarioRepository):
        self.inventario_repository = inventario_repository

    async def get_all_inventario(self) -> list[MaterialDomain]:
        return self.inventario_repository.get_all()

    async def get_inventario_by_id(self, id_material: int):
        return self.inventario_repository.get_by_id(id_material)

    async def add_inventario(self, inventario: InventarioDomain):
        return self.inventario_repository.add(inventario)

    async def remove_inventario(self, id_material: int):
        return self.inventario_repository.remove(id_material)
