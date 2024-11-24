from src.core.abstractions.infrastructure.repository.usuario_repository_abstract import IUsuarioRepository
from src.core.abstractions.services.usuario_service_abstract import IUsuarioService
from src.core.models.usuario_domain import UsuarioDomain


class usuarioService(IUsuarioService):

    def __init__(self, usuario_repository: IUsuarioRepository):
        self.usuario_repository = usuario_repository

    async def get_all_usuario(self) -> list[UsuarioDomain]:
        return await self.usuario_repository.get_all()

    async def get_usuario_by_id(self, usuario_id: int) -> UsuarioDomain:
        return await self.usuario_repository.get_by_id(usuario_id)

    async def register_usuario(self, usuario: UsuarioDomain) -> bool:
        return await self.usuario_repository.register(usuario)
    
    async def login_usuario(self, email: str, password: str) -> UsuarioDomain:
        return await self.usuario_repository.login(email, password)

    async def update_usuario(self, usuario_id: int, usuario: UsuarioDomain):
        return await self.usuario_repository.update(usuario_id, usuario)

    async def delete_usuario(self, usuario_id: int) -> bool:
        return await self.usuario_repository.delete(usuario_id)
