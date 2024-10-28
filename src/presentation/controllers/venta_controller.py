from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.venta_service_abstract import IVentaService
from src.core.dependency_inyection.dependency_inyection import build_venta_service

from src.presentation.dto.venta_dto import VentaDTO
from src.presentation.mappers.map_dto_domain_venta import map_domain_dto_to_venta


venta_controller = APIRouter(prefix="/api/v1", tags=["venta"])


@venta_controller.get("/venta")
async def get_all_venta(
        venta_service: IVentaService = Depends(build_venta_service)
):
    try:
        venta = await venta_service.get_all_venta()
        return venta
    except Exception as e:
        return {"error": str(e)}

@venta_controller.get("/venta/{venta_id}")
async def get_venta_by_id(
        venta_id: int,
        venta_service: IVentaService = Depends(build_venta_service)
):
    try:
        venta = await venta_service.get_venta_by_id(venta_id)
        return venta
    except Exception as e:
        return {"error": str(e)}

@venta_controller.post("/venta")
async def create_venta(
        ventaDTO: VentaDTO,
        venta_service: IVentaService = Depends(build_venta_service)
):
    """
    :type ventaDTO: VentaDTO
    :type venta_service: IVentaService
    """
    try:
        venta = map_domain_dto_to_venta(ventaDTO)
        await venta_service.create_venta(venta)
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}

@venta_controller.put("/venta/{venta_id}")
async def update_venta(
        venta_id: int,
        ventaDTO: VentaDTO,
        venta_service: IVentaService = Depends(build_venta_service)
):
    """
    :type venta_id: int
    :type ventaDTO: VentaDTO
    :type venta_service: IVentaService
    """
    try:
        venta = map_domain_dto_to_venta(ventaDTO)
        await venta_service.update_venta(venta_id, venta)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}

@venta_controller.delete("/venta/{venta_id}")
async def delete_venta(
        venta_id: int,
        venta_service: IVentaService = Depends(build_venta_service)
):
    try:
        await venta_service.delete_venta(venta_id)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}

