from abc import ABC, abstractmethod
from src.core.models.usuario_domain import UsuarioDomain


class IUsuarioRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[UsuarioDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, id_usr: int) -> UsuarioDomain:
        pass

    @abstractmethod
    async def register(self, usr: UsuarioDomain) -> bool:
        pass
    
    @abstractmethod
    async def login(self, email: str, password: str) -> UsuarioDomain:
        pass

    @abstractmethod
    async def update(self, id_usr: int, usr: UsuarioDomain):
        pass

    @abstractmethod
    async def delete(self, id_usr: int) -> bool:
        pass
