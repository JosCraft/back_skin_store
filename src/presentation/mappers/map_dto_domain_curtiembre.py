from src.core.models.curtiembre_domain import CurtiembreDomain
from src.presentation.dto.curtiembre_dto import CurtiembreDTO


def map_domain_dto_to_curtiembre(curtiembreDTO: CurtiembreDTO) -> CurtiembreDomain:
    return CurtiembreDomain(
        id=curtiembreDTO.id,
        nombre=curtiembreDTO.nombre,
        numero=curtiembreDTO.numero
    )
