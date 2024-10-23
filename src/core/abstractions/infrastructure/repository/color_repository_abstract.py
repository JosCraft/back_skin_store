from abc import ABC, abstractmethod

from src.core.models.color_domain import ColorDomain


class IColorRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[ColorDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, color_id) -> ColorDomain:
        pass

    @abstractmethod
    async def create(self, color: ColorDomain):
        pass

    @abstractmethod
    async def update(self, color_id: int, color: ColorDomain):
        pass

    @abstractmethod
    async def delete(self, color_id) -> bool:
        pass
