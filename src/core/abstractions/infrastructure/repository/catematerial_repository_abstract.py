from abc import ABC, abstractmethod

from src.core.models.catematerial_domain import CateMaterialDomain


class ICateMaterialRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[CateMaterialDomain]:
        pass

    @abstractmethod
    async def add(self, catematerial: CateMaterialDomain):
        pass

    @abstractmethod
    async def remove(self, catematerial_id) -> bool:
        pass
