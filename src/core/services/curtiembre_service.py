from src.core.abstractions.infrastructure.repository.curtiembre_repository_abstract import ICurtiembreRepository
from src.core.abstractions.services.curtiembre_service_abstract import ICurtiembreService
from src.core.models.curtiembre_domain import CurtiembreDomain


class curtiembreService(ICurtiembreService):

    def __init__(self, curtiembre_repository: ICurtiembreRepository):
        self.curtiembre_repository = curtiembre_repository

    async def get_all_curtiembre(self) -> list[CurtiembreDomain]:
        return await self.curtiembre_repository.get_all()

    async def get_curtiembre_by_id(self, curtiembre_id: int) -> CurtiembreDomain:
        return await self.curtiembre_repository.get_by_id(curtiembre_id)

    async def create_curtiembre(self, curtiembre: CurtiembreDomain):
        await self.curtiembre_repository.create(curtiembre)

    async def update_curtiembre(self, id_curtiembre: int,  curtiembre: CurtiembreDomain):
        await self.curtiembre_repository.update(id_curtiembre, curtiembre)

    async def delete_curtiembre(self, curtiembre_id: int):
        return await self.curtiembre_repository.delete(curtiembre_id)
