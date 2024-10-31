from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.presentation.dto.ventamaterial_dto import VentaMaterialDTO
from src.core.models.material_domain import MaterialDomain
from src.core.models.venta_domain import VentaDomain

def map_dto_domain_to_ventamaterial(ventaMaterialDTO : VentaMaterialDTO ) -> VentaMaterialDomain:
    return VentaMaterialDomain(
        idVenta=ventaMaterialDTO.idVenta,
        idMaterial=ventaMaterialDTO.idMaterial,
        MaterialDomain=None,
        VentaDomain=None,
    )
