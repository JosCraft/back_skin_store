from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.tipo_service_abstract import ITipoService
from src.core.dependency_inyection.dependency_inyection import build_tipo_service

from src.presentation.dto.tipo_dto import TipoDTO
from src.presentation.mappers.map_dto_domain_tipo import map_domain_dto_to_tipo

tipo_controller = APIRouter(prefix="/api/v1", tags=["tipo"])


@tipo_controller.get("/tipo")
async def get_all_tipo(
        tipo_service: ITipoService = Depends(build_tipo_service)
):
    try:
        tipo = await tipo_service.get_all_tipo()
        return tipo
    except Exception as e:
        return {"error": str(e)}


@tipo_controller.get("/tipo/{tipo_id}")
async def get_tipo_by_id(
        tipo_id: int,
        tipo_service: ITipoService = Depends(build_tipo_service)
):
    try:
        tipo = await tipo_service.get_tipo_by_id(tipo_id)
        return tipo
    except Exception as e:
        return {"error": str(e)}


@tipo_controller.post("/tipo")
async def create_tipo(
        tipoDTO: TipoDTO,
        tipo_service: ITipoService = Depends(build_tipo_service)
):
    """
    :type tipoDTO: TipoDTO
    :type tipo_service: ITipoService
    """
    try:
        tipo = map_domain_dto_to_tipo(tipoDTO)
        await tipo_service.create_tipo(tipo)
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}


@tipo_controller.put("/tipo/{tipo_id}")
async def update_tipo(
        tipo_id: int,
        tipoDTO: TipoDTO,
        tipo_service: ITipoService = Depends(build_tipo_service)
):
    """
    :type tipo_id: int
    :type tipoDTO: TipoDTO
    :type tipo_service: ITipoService
    """
    try:
        tipo = map_domain_dto_to_tipo(tipoDTO)
        await tipo_service.update_tipo(tipo_id, tipo)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}


@tipo_controller.delete("/tipo/{tipo_id}")
async def delete_tipo(
        tipo_id: int,
        tipo_service: ITipoService = Depends(build_tipo_service)
):
    try:
        await tipo_service.delete_tipo(tipo_id)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}
