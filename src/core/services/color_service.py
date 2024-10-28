from src.core.abstractions.infrastructure.repository.color_repository_abstract import IColorRepository
from src.core.abstractions.services.color_service_abstract import IColorService
from src.core.models.color_domain import ColorDomain


class colorService(IColorService):

    def __init__(self, color_repository: IColorRepository):
        self.color_repository = color_repository

    async def get_all_color(self) -> list[ColorDomain]:
        return await self.color_repository.get_all()

    async def get_color_by_id(self, color_id: int) -> ColorDomain:
        return await self.color_repository.get_by_id(color_id)

    async def create_color(self, color: ColorDomain):
        await self.color_repository.create(color)

    async def update_color(self, color_id: int, color: ColorDomain):
        await self.color_repository.update(color_id, color)

    async def delete_color(self, color_id: int) -> bool:
        return await self.color_repository.delete(color_id)
