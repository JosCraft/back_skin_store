from fastapi import Depends

from src.core.services.color_service import colorService
from src.core.services.curtiembre_service import curtiembreService
from src.core.services.tipo_service import tipoService
from src.core.services.material_service import materialService
from src.core.services.inventario_service import inventarioService
from src.core.services.venta_service import ventaService
from src.core.services.ventaMaterial_service import ventamaterialService
from src.core.services.catematerial_service import CateMaterialService
from src.core.services.usuario_service import usuarioService
from src.core.services.dashboard_service import dashboardService

from src.infrastructure.repository.dependency_inyection.dependency_inyection import get_db_connection

from src.infrastructure.repository.implementations.color_repository import colorRepository
from src.infrastructure.repository.implementations.curtiembre_repository import CurtiembreRepository
from src.infrastructure.repository.implementations.tipo_repository import tipoRepository
from src.infrastructure.repository.implementations.material_repository import MaterialRepository
from src.infrastructure.repository.implementations.inventario_repository import InventarioRepository
from src.infrastructure.repository.implementations.venta_repository import ventaRepository
from src.infrastructure.repository.implementations.ventamaterial_repository import VentaMaterialRepository
from src.infrastructure.repository.implementations.catematerial_repository import cateMaterialRepository
from src.infrastructure.repository.implementations.usuario_repository import usuarioRepository
from src.infrastructure.repository.implementations.dashboard_repository import DashboardRepository

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


def build_material_service(
        db_connection=Depends(get_db_connection)
):
    return materialService(MaterialRepository(db_connection))


def build_inventario_service(
        db_connection=Depends(get_db_connection)
):
    return inventarioService(InventarioRepository(db_connection))


def build_venta_service(
        db_connection=Depends(get_db_connection)
):
    return ventaService(ventaRepository(db_connection))


def build_ventamaterial_service(
        db_connection=Depends(get_db_connection)
):
    return ventamaterialService(VentaMaterialRepository(db_connection))


def build_catematerial_service(
        db_connection=Depends(get_db_connection)
):
    return CateMaterialService(cateMaterialRepository(db_connection))


def build_usuario_service(db_connection=Depends(get_db_connection)):        
        return usuarioService(usuarioRepository(db_connection))

def build_dashboard_service(db_connection=Depends(get_db_connection)):        
        return dashboardService(DashboardRepository(db_connection))