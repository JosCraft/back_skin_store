from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.curtiembre_service_abstract import ICurtiembreService
from src.core.dependency_inyection.dependency_inyection import build_curtiembre_service

from src.presentation.dto.curtiembre_dto import CurtiembreDTO
from src.presentation.mappers.map_dto_domain_curtiembre import map_domain_dto_to_curtiembre

curtiembre_controller = APIRouter(prefix="/api/v1", tags=["curtiembre"])


@curtiembre_controller.get("/curtiembre")
async def get_curtiembre(
        curtiembre_service: ICurtiembreService = Depends(build_curtiembre_service)
):
    try:
        curtiembre = await curtiembre_service.get_all_curtiembre()
        return curtiembre
    except Exception as e:
        return {"error": str(e)}


@curtiembre_controller.get("/curtiembre/{curtiembre_id}")
async def get_curtiembre_by_id(
        curtiembre_id: int,
        curtiembre_service: ICurtiembreService = Depends(build_curtiembre_service)
):
    try:
        curtiembre = await curtiembre_service.get_curtiembre_by_id(curtiembre_id)
        return curtiembre
    except Exception as e:
        return {"error": str(e)}


@curtiembre_controller.post("/curtiembre")
async def create_curtiembre(
        curtiembreDTO: CurtiembreDTO,
        curtiembre_service: ICurtiembreService = Depends(build_curtiembre_service)
):
    """
    :type curtiembreDTO: CurtiembreDTO
    :type curtiembre_service: ICurtiembreService
    """
    try:
        curtiembre = map_domain_dto_to_curtiembre(curtiembreDTO)
        await curtiembre_service.create_curtiembre(curtiembre)
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}


@curtiembre_controller.put("/curtiembre/{curtiembre_id}")
async def update_curtiembre(
        curtiembre_id: int,
        curtiembreDTO: CurtiembreDTO,
        curtiembre_service: ICurtiembreService = Depends(build_curtiembre_service)
):
    """
    :type curtiembre_id: int
    :type curtiembreDTO: CurtiembreDTO
    :type curtiembre_service: ICurtiembreService
    """
    try:
        curtiembre = map_domain_dto_to_curtiembre(curtiembreDTO)
        await curtiembre_service.update_curtiembre(curtiembre_id, curtiembre)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}


@curtiembre_controller.delete("/curtiembre/{curtiembre_id}")
async def delete_curtiembre(
        curtiembre_id: int,
        curtiembre_service: ICurtiembreService = Depends(build_curtiembre_service)
):
    """
    :type curtiembre_id: int
    :type curtiembre_service: ICurtiembreService
    """
    try:
        await curtiembre_service.delete_curtiembre(curtiembre_id)
        return Response(status_code=204)
    except Exception as e:
        return {"error": str(e)}
