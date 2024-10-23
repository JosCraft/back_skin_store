from abc import ABC, abstractmethod

from src.core.models.curtiembre_domain import CurtiembreDomain


class ICurtiembreRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[CurtiembreDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> CurtiembreDomain:
        pass

    @abstractmethod
    async def create(self, curt: CurtiembreDomain):
        pass

    @abstractmethod
    async def update(self, id: int, curt: CurtiembreDomain):
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass
