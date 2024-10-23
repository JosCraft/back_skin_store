from abc import ABC, abstractmethod
from src.core.models.color_domain import ColorDomain


class IColorService(ABC):
    @abstractmethod
    async def get_all_color(self) -> list[ColorDomain]:
        pass

    @abstractmethod
    async def get_color_by_id(self, color_id: int) -> ColorDomain:
        pass

    @abstractmethod
    async def create_color(self, color: ColorDomain):
        pass

    @abstractmethod
    async def update_color(self, color_id: int, color: ColorDomain):
        pass

    @abstractmethod
    async def delete_color(self, color_id: int) -> bool:
        pass