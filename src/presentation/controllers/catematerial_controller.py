from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.catematerial_service_abstract import ICateMaterialService
from src.core.dependency_inyection.dependency_inyection import build_catematerial_service

from src.presentation.dto.catematerial_dto import CateMaterialDTO
from src.presentation.mappers.map_dto_domain_catematerial import map_domain_dto_to_catematerial

catematerial_controller = APIRouter(prefix="/api/v1", tags=["catematerial"])


@catematerial_controller.get("/catematerial")
async def get_cate(
        catematerial_service: ICateMaterialService = Depends(build_catematerial_service)
):
    try:
        cate = await catematerial_service.get_all_cate()
        return cate
    except Exception as e:
        return {"error": str(e)}


@catematerial_controller.post("/catematerial")
async def create_cate(
        catematerialDTO: CateMaterialDTO,
        catematerial_service: ICateMaterialService = Depends(build_catematerial_service)
):
    """
    :type catematerialDTO: CateMaterialDTO
    :type catematerial_service: ICateMaterialService
    """
    try:
        cate = map_domain_dto_to_catematerial(catematerialDTO)
        await catematerial_service.add_cate(cate)
        return Response(status_code=201)
    except Exception as e:
        return {"error": str(e)}


@catematerial_controller.delete("/catematerial/{catematerial_id}")
async def delete_cate(
        catematerial_id: int,
        catematerial_service: ICateMaterialService = Depends(build_catematerial_service)
):
    try:
        await catematerial_service.remove_cate(catematerial_id)
        return Response(status_code=200)
    except Exception as e:
        return {"error": str(e)}
