from src.core.models.inventario_domain import InventarioDomain
from src.presentation.dto.inventario_dto import InventarioDTO


def map_domain_dto_to_inventario(inventarioDTO: InventarioDTO) -> InventarioDomain:
    return InventarioDomain(
        idInventario=inventarioDTO.idInventario,
        idMaterial=inventarioDTO.idMaterial
    )
