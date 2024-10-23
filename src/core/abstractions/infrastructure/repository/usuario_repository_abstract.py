from abc import ABC, abstractmethod
from src.core.models.usuario_domain import UsuarioDomain


class IUsuarioRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[UsuarioDomain]:
        pass

    @abstractmethod
    def get_by_id(self, id_usr: int) -> UsuarioDomain:
        pass

    @abstractmethod
    def create(self, usr: UsuarioDomain):
        pass

    @abstractmethod
    def update(self, id_usr: int, usr: UsuarioDomain):
        pass

    @abstractmethod
    def delete(self, id_usr: int) -> bool:
        pass
