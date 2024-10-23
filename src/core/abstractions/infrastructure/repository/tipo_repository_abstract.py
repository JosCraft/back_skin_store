from abc import ABC, abstractmethod

from src.core.models.tipo_domain import TipoDomain


class ITipoRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[TipoDomain]:
        pass

    @abstractmethod
    def get_by_id(self, id_tipo: int) -> TipoDomain:
        pass

    @abstractmethod
    def create(self, tip: TipoDomain):
        pass

    @abstractmethod
    def update(self, id_tipo: int, tip: TipoDomain):
        pass

    @abstractmethod
    def delete(self, id_tipo: int) -> bool:
        pass
