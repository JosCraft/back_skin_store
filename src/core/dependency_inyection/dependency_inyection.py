from fastapi import Depends

from src.core.services.color_service import colorService
from src.core.services.curtiembre_service import curtiembreService
from src.core.services.tipo_service import tipoService

from src.infrastructure.repository.dependency_inyection.dependency_inyection import get_db_connection

from src.infrastructure.repository.implementations.color_repository import colorRepository
from src.infrastructure.repository.implementations.curtiembre_repository import CurtiembreRepository
from src.infrastructure.repository.implementations.tipo_repository import tipoRepository


def build_curtiembre_service(
        db_connection=Depends(get_db_connection)
):
    return curtiembreService(CurtiembreRepository(db_connection))


def build_color_service(
        db_connection=Depends(get_db_connection)
):
    return colorService(colorRepository(db_connection))


def build_tipo_service(
        db_connection=Depends(get_db_connection)
):
    return tipoService(tipoRepository(db_connection))
