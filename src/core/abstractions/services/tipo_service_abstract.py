from abc import ABC, abstractmethod
from src.core.models.tipo_domain import TipoDomain


class ITipoService(ABC):
    @abstractmethod
    async def get_all_tipo(self) -> list[TipoDomain]:
        pass

    @abstractmethod
    async def get_tipo_by_id(self, tipo_id: int) -> TipoDomain:
        pass

    @abstractmethod
    async def create_tipo(self, tipo: TipoDomain):
        pass

    @abstractmethod
    async def update_tipo(self, tipo_id: int, tipo: TipoDomain):
        pass

    @abstractmethod
    async def delete_tipo(self, tipo_id: int) -> bool:
        pass
