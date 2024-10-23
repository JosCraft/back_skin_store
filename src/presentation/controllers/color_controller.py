from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.color_service_abstract import IColorService
from src.core.dependency_inyection.dependency_inyection import build_color_service

from src.presentation.dto.color_dto import ColorDTO
from src.presentation.mappers.map_dto_domain_color import map_domain_dto_to_color

color_controller = APIRouter(prefix="/api/v1", tags=["color"])


@color_controller.get("/color")
async def get_color(
        color_service: IColorService = Depends(build_color_service)
):
    try:
        color = await color_service.get_all_color()
        return color
    except Exception as e:
        return {"error": str(e)}


@color_controller.get("/color/{color_id}")
async def get_color_by_id(
        color_id: int,
        color_service: IColorService = Depends(build_color_service)
):
    try:
        color = await color_service.get_color_by_id(color_id)
        return color
    except Exception as e:
        return {"error": str(e)}


@color_controller.post("/color")
async def create_color(
        colorDTO: ColorDTO,
        color_service: IColorService = Depends(build_color_service)
):
    """
    :type colorDTO: ColorDTO
    :type color_service: IColorService
    """
    try:
        color = map_domain_dto_to_color(colorDTO)
        await color_service.create_color(color)
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}


@color_controller.put("/color/{color_id}")
async def update_color(
        color_id: int,
        colorDTO: ColorDTO,
        color_service: IColorService = Depends(build_color_service)
):
    """
    :type color_id: int
    :type colorDTO: ColorDTO
    :type color_service: IColorService
    """
    try:
        color = map_domain_dto_to_color(colorDTO)
        await color_service.update_color(color_id, color)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}


@color_controller.delete("/color/{color_id}")
async def delete_color(
        color_id: int,
        color_service: IColorService = Depends(build_color_service)
):
    try:
        await color_service.delete_color(color_id)
        return Response(status_code=204)
    except Exception as e:
        return {"error": str(e)}
