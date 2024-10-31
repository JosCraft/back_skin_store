from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.ventaMaterial_service_abstract import IVentaMaterialService
from src.core.dependency_inyection.dependency_inyection import build_ventamaterial_service

from src.presentation.dto.ventamaterial_dto import VentaMaterialDTO
from src.presentation.mappers.map_dto_domain_ventamaterial import map_dto_domain_to_ventamaterial


ventamaterial_controller = APIRouter(prefix="/api/v1", tags=["ventamaterial"])


@ventamaterial_controller.get("/ventamaterial")
async def get_all_ventamaterial(
        ventamaterial_service: IVentaMaterialService = Depends(build_ventamaterial_service)
):
    try:
        ventamaterial = await ventamaterial_service.get_all_ventamaterial()
        return ventamaterial
    except Exception as e:
        return {"error": str(e)}


@ventamaterial_controller.get("/ventamaterial/{ventamaterial_id}")
async def get_ventamaterial_by_id(
        ventamaterial_id: int,
        ventamaterial_service: IVentaMaterialService = Depends(build_ventamaterial_service)
):
    try:
        ventamaterial = await ventamaterial_service.get_ventamaterial_by_id(ventamaterial_id)
        return ventamaterial
    except Exception as e:
        return {"error": str(e)}


@ventamaterial_controller.post("/ventamaterial")
async def create_ventamaterial(
        ventamaterialDTO: VentaMaterialDTO,
        ventamaterial_service: IVentaMaterialService = Depends(build_ventamaterial_service)
):
    """
    :type ventamaterialDTO: VentaMaterialDTO
    :type ventamaterial_service: IVentaMaterialService
    """
    try:
        print(ventamaterialDTO)
        ventamaterial = map_dto_domain_to_ventamaterial(ventamaterialDTO)
        await ventamaterial_service.add_ventamaterial(ventamaterial)
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}


@ventamaterial_controller.delete("/ventamaterial/{material_id}")
async def remove_ventamaterial(
        material_id: int,
        ventamaterial_service: IVentaMaterialService = Depends(build_ventamaterial_service)
):
    try:
        await ventamaterial_service.remove_ventamaterial(ventamaterial_id)
        return Response(status_code=204)
    except Exception as e:
        return {"error": str(e)}

