from abc import ABC, abstractmethod
from src.core.models.curtiembre_domain import CurtiembreDomain
from src.core.abstractions.infrastructure.repository.curtiembre_repository_abstract import ICurtiembreRepository

class ICurtiembreService(ABC):
    @abstractmethod
    async def get_all_curtiembre(self) -> list[CurtiembreDomain]:
        pass

    @abstractmethod
    async def get_curtiembre_by_id(self, curtiembre_id: int) -> CurtiembreDomain:
        pass

    @abstractmethod
    async def create_curtiembre(self, curtiembre: CurtiembreDomain):
        pass

    @abstractmethod
    async def update_curtiembre(self, curtiembre_id: int, curtiembre: CurtiembreDomain):
        pass

    @abstractmethod
    async def delete_curtiembre(self, curtiembre_id: int) -> bool:
        pass
