from src.core.abstractions.infrastructure.repository.dahsboard_repository_abstract import *
from src.core.abstractions.services.dashboard_service_abstract import IDashboardService



class dashboardService(IDashboardService):

    def __init__(self, dashboard_repository: IDashboardRepository):
        self.dashboard_repository = dashboard_repository

    async def get_dashboard_counts(self) -> StatsDomain:
        return await self.dashboard_repository.get_counts()

    async def get_dashboard_ventas_plot(self) -> list[ventaPlotDomain]:
        return await self.dashboard_repository.get_ventas_plot()
    
    async def get_dashboard_ganancias_plot(self) -> list[GananciasDomain]:
        return await self.dashboard_repository.get_ganancias_plot()
    
    async def get_dashboard_material_by_sell(self) -> list[TipoDomain]:
        return await self.dashboard_repository.get_material_by_sell()
    
    async def get_dashboard_material_by_gain(self) -> list[TipoDomain]:
        return await self.dashboard_repository.get_material_by_gain()
    
    