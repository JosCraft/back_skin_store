from src.core.models.tipo_domain import TipoDomain
from src.presentation.dto.tipo_dto import TipoDTO


def map_domain_dto_to_tipo(tipoDTO: TipoDTO) -> TipoDomain:
    return TipoDomain(
        nombre=tipoDTO.nombre,
        precio=tipoDTO.precio,
        idCategoria=tipoDTO.idCategoria,
        idColor=tipoDTO.idColor,
        idCurtiembre=tipoDTO.idCurtiembre
    )

