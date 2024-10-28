from src.core.models.material_domain import MaterialDomain
from src.presentation.dto.material_dto import MaterialDTO


def map_domain_dto_to_material(materialDTO: MaterialDTO) -> MaterialDomain:
    return MaterialDomain(
        id=materialDTO.id,
        medida=materialDTO.medida,
        idTipo=materialDTO.idTipo
    )
