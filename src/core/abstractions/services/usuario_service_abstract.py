from abc import ABC, abstractmethod
from src.core.models.usuario_domain import UsuarioDomain


class IUsuarioService(ABC):
    @abstractmethod
    async def get_all_usuario(self) -> list[UsuarioDomain]:
        pass

    @abstractmethod
    async def get_usuario_by_id(self, usuario_id: int) -> UsuarioDomain:
        pass

    @abstractmethod
    async def register_usuario(self, usuario: UsuarioDomain) -> bool:
        pass
    
    @abstractmethod
    async def login_usuario(self, email: str, password: str) -> UsuarioDomain:
        pass

    @abstractmethod
    async def update_usuario(self, usuario_id: int, usuario: UsuarioDomain):
        pass

    @abstractmethod
    async def delete_usuario(self, usuario_id: int) -> bool:
        pass
