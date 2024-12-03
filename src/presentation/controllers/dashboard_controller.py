from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.dashboard_service_abstract import *
from src.core.dependency_inyection.dependency_inyection import build_dashboard_service

dashboard_controller = APIRouter(prefix="/api/v1", tags=["dashboard"])

@dashboard_controller.get("/dashboard/counts")
async def get_dashboard_counts(
        dashboard_service: IDashboardService = Depends(build_dashboard_service)
):
    try:
        counts = await dashboard_service.get_dashboard_counts()
        return counts
    except Exception as e:
        return {"error": str(e)}
    
@dashboard_controller.get("/dashboard/ventas_plot")
async def get_ventas_plot(
        dashboard_service: IDashboardService = Depends(build_dashboard_service)
):
    try:
        ventas_plot = await dashboard_service.get_dashboard_ventas_plot()
        return ventas_plot
    except Exception as e:
        return {"error": str(e)}
    
@dashboard_controller.get("/dashboard/ganancias_plot")
async def get_ganancias_plot(
        dashboard_service: IDashboardService = Depends(build_dashboard_service)
):
    try:
        ganancias_plot = await dashboard_service.get_dashboard_ganancias_plot()
        return ganancias_plot
    except Exception as e:
        return {"error": str(e)}
    
@dashboard_controller.get("/dashboard/material_by_sell")
async def get_ganancias(
        dashboard_service: IDashboardService = Depends(build_dashboard_service)
):
    try:
        ganancias = await dashboard_service.get_dashboard_material_by_sell()
        return ganancias
    except Exception as e:
        return {"error": str(e)}
    
@dashboard_controller.get("/dashboard/material_by_gain")
async def get_ganancias(
        dashboard_service: IDashboardService = Depends(build_dashboard_service)
):
    try:
        ganancias = await dashboard_service.get_dashboard_material_by_gain()
        return ganancias
    except Exception as e:
        return {"error": str(e)}
    