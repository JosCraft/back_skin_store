from src.core.abstractions.infrastructure.repository.catematerial_repository_abstract import ICateMaterialRepository
from src.core.abstractions.services.catematerial_service_abstract import ICateMaterialService
from src.core.models.catematerial_domain import CateMaterialDomain


class CateMaterialService(ICateMaterialService):

    def __init__(self, catematerial_repository: ICateMaterialRepository):
        self.catematerial_repository = catematerial_repository

    async def get_all_cate(self) -> list[CateMaterialDomain]:
        return await self.catematerial_repository.get_all()

    async def add_cate(self, catematerial: CateMaterialDomain):
        await self.catematerial_repository.add(catematerial)

    async def remove_cate(self, catematerial_id) -> bool:
        return await self.catematerial_repository.remove(catematerial_id)
