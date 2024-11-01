from abc import ABC, abstractmethod
from src.core.models.catematerial_domain import CateMaterialDomain


class ICateMaterialService(ABC):

    @abstractmethod
    async def get_all_cate(self) -> list[CateMaterialDomain]:
        pass

    @abstractmethod
    async def add_cate(self, catematerial: CateMaterialDomain):
        pass

    @abstractmethod
    async def remove_cate(self, catematerial_id) -> bool:
        pass
