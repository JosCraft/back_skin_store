from src.core.abstractions.infrastructure.repository.usuario_repository_abstract import IUsuarioRepository
from src.core.abstractions.services.usuario_service_abstract import IUsuarioService
from src.core.models.usuario_domain import UsuarioDomain

class usuarioService(IUsuarioService):

    def __init__(self, usuario_repository: IUsuarioRepository):
            self.usuario_repository = usuario_repository

    async def get_all_usuario(self):
        return self.usuario_repository.get_all_usuario()

    async def get_usuario_by_id(self, id: int):
        return self.usuario_repository.get_usuario_by_id(id)

    async def create_usuario(self, usuario: UsuarioDomain):
        return self.usuario_repository.create_usuario(usuario)

    async def update_usuario(self, id: int, usuario: UsuarioDomain):
        return self.usuario_repository.update_usuario(id, usuario)

    async def delete_usuario(self, id: int):
        return self.usuario_repository.delete_usuario(id)