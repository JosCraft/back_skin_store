from src.core.abstractions.infrastructure.repository.usuario_repository_abstract import IUsuarioRepository
from src.core.abstractions.services.usuario_service_abstract import IUsuarioService
from src.core.models.usuario_domain import UsuarioDomain


class usuarioService(IUsuarioService):

    def __init__(self, usuario_repository: IUsuarioRepository):
        self.usuario_repository = usuario_repository

    async def get_all_usuario(self) -> list[UsuarioDomain]:
        return self.usuario_repository.get_all()

    async def get_usuario_by_id(self, usuario_id: int) -> UsuarioDomain:
        return self.usuario_repository.get_by_id(usuario_id)

    async def create_usuario(self, usuario: UsuarioDomain):
        return self.usuario_repository.create(usuario)

    async def update_usuario(self, usuario_id: int, usuario: UsuarioDomain):
        return self.usuario_repository.update(usuario_id, usuario)

    async def delete_usuario(self, usuario_id: int) -> bool:
        return self.usuario_repository.delete(usuario_id)
