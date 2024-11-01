from src.core.models.catematerial_domain import CateMaterialDomain
from src.presentation.dto.catematerial_dto import CateMaterialDTO


def map_domain_dto_to_catematerial(catematerialDTO: CateMaterialDTO) -> CateMaterialDomain:
    return CateMaterialDomain(
        id=catematerialDTO.id,
        nombre=catematerialDTO.nombre,
        medida=catematerialDTO.medida
   )
