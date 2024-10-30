from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.presentation.dto.ventamaterial_dto import VentaMaterialDTO


def map_dto_domain_to_ventamaterial(ventaMaterialDTO: VentaMaterialDTO) -> VentaMaterialDomain:
    return VentaMaterialDomain(
        idVenta=ventaMaterialDTO.idVenta,
        idMaterial=ventaMaterialDTO.idMaterial
    )
