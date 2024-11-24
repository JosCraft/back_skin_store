from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.material_service_abstract import IMaterialService
from src.core.abstractions.services.inventario_service_abstract import IInventarioService
from src.core.dependency_inyection.dependency_inyection import build_material_service
from src.core.dependency_inyection.dependency_inyection import build_inventario_service

from src.presentation.dto.material_dto import MaterialDTO
from src.presentation.dto.inventario_dto import InventarioDTO
from src.core.models.inventario_domain import InventarioDomain
from src.presentation.mappers.map_dto_domain_material import map_domain_dto_to_material
from src.presentation.mappers.map_dto_domain_inventario import map_domain_dto_to_inventario

material_controller = APIRouter(prefix="/api/v1", tags=["material"])


@material_controller.get("/material")
async def get_all_by_tipo_material(
        id_tipo: int,
        material_service: IMaterialService = Depends(build_material_service)
):
    try:
        material = await material_service.get_all_by_tipo_material(id_tipo)
        return material
    except Exception as e:
        return {"error": str(e)}


@material_controller.get("/material/{material_id}")
async def get_material_by_id(
        material_id: int,
        material_service: IMaterialService = Depends(build_material_service)
):
    try:
        material = await material_service.get_material_by_id(material_id)
        return material
    except Exception as e:
        return {"error": str(e)}


@material_controller.post("/material")
async def create_material(
        materialDTO: MaterialDTO,
        material_service: IMaterialService = Depends(build_material_service),
        inventario_service: IInventarioService = Depends(build_inventario_service)
):
    """
    :type materialDTO: MaterialDTO
    :type material_service: IMaterialService
    """
    try:
        material = map_domain_dto_to_material(materialDTO)
        idMaterial = await material_service.create_material(material)
        await inventario_service.add_inventario(InventarioDomain(idMaterial=idMaterial, idInventario=0))
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}


@material_controller.put("/material/{material_id}")
async def update_material(
        material_id: int,
        materialDTO: MaterialDTO,
        material_service: IMaterialService = Depends(build_material_service)
):
    """
    :type material_id: int
    :type materialDTO: MaterialDTO
    :type material_service: IMaterialService
    """
    try:
        material = map_domain_dto_to_material(materialDTO)
        await material_service.update_material(material_id, material)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}


@material_controller.delete("/material/{material_id}")
async def delete_material(
        material_id: int,
        material_service: IMaterialService = Depends(build_material_service)
):
    try:
        await material_service.delete_material(material_id)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}

