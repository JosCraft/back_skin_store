from src.core.models.venta_domain import VentaDomain
from src.presentation.dto.venta_dto import VentaDTO


def map_domain_dto_to_venta(ventaDTO: VentaDTO) -> VentaDomain:
    return VentaDomain(
        id=ventaDTO.id,
        fecha=ventaDTO.fecha,
        total=ventaDTO.total
    )