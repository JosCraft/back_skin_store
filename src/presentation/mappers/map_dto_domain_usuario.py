from src.core.models.usuario_domain import UsuarioDomain
from src.presentation.dto.usuario_dto import UsuarioDTO

def map_domain_dto_to_usuario(usuarioDTO: UsuarioDTO) -> UsuarioDomain:
    return UsuarioDomain(
        id=usuarioDTO.id,
        nombre=usuarioDTO.nombre,
        apelldio=usuarioDTO.apelldio,
        numero=usuarioDTO.numero,
        email=usuarioDTO.email,
        password=usuarioDTO.password,
        activo= True,
        role='USER'
    )
    