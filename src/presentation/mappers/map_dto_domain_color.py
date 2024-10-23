from src.core.models.color_domain import ColorDomain
from src.presentation.dto.color_dto import ColorDTO


def map_domain_dto_to_color(colorDTO: ColorDTO) -> ColorDomain:
    return ColorDomain(
        id=colorDTO.id,
        nombre=colorDTO.nombre,
        codigoHex=colorDTO.codigo
   )
