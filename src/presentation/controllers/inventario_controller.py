from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.inventario_service_abstract import IInventarioService
from src.core.dependency_inyection.dependency_inyection import build_inventario_service

from src.presentation.dto.inventario_dto import InventarioDTO
from src.presentation.mappers.map_dto_domain_inventario import map_domain_dto_to_inventario

inventario_controller = APIRouter(prefix="/api/v1", tags=["inventario"])


@inventario_controller.get("/inventario")
async def get_inventario(
        inventario_service: IInventarioService = Depends(build_inventario_service)
):
    try:
        inventario = await inventario_service.get_all_inventario()
        return inventario
    except Exception as e:
        return {"error": str(e)}


@inventario_controller.get("/inventario/{inventario_id}")
async def get_inventario_by_id(
        inventario_id: int,
        inventario_service: IInventarioService = Depends(build_inventario_service)
):
    try:
        inventario = await inventario_service.get_inventario_by_id(inventario_id)
        return inventario
    except Exception as e:
        return {"error": str(e)}


@inventario_controller.post("/inventario")
async def create_inventario(
        inventarioDTO: InventarioDTO,
        inventario_service: IInventarioService = Depends(build_inventario_service)
):
    """
    :type inventarioDTO: InventarioDTO
    :type inventario_service: IInventarioService
    """
    try:
        inventario = map_domain_dto_to_inventario(inventarioDTO)
        await inventario_service.add_inventario(inventario)
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}


@inventario_controller.delete("/inventario/{inventario_id}")
async def delete_inventario(
        inventario_id: int,
        inventario_service: IInventarioService = Depends(build_inventario_service)
):
    try:
        await inventario_service.remove_inventario(inventario_id)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}