from abc import ABC, abstractmethod

from src.core.models.tipo_domain import TipoDomain


class ITipoRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[TipoDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, id_tipo: int) -> TipoDomain:
        pass

    @abstractmethod
    async def create(self, tip: TipoDomain):
        pass

    @abstractmethod
    async def update(self, id_tipo: int, tip: TipoDomain):
        pass

    @abstractmethod
    async def delete(self, id_tipo: int) -> bool:
        pass
