from abc import ABC, abstractmethod
from src.core.models.stats_domain import StatsDomain
from src.core.models.ventaPlot_domain import ventaPlotDomain
from src.core.models.gananciasPlot_domain import GananciasDomain
from src.core.models.tipo_domain import TipoDomain

class IDashboardService(ABC):

    @abstractmethod
    async def get_dashboard_counts(self) -> StatsDomain:
        pass

    @abstractmethod
    async def get_dashboard_ventas_plot(self) -> list[ventaPlotDomain]:
        pass
    
    @abstractmethod
    async def get_dashboard_ganancias_plot(self) -> list[GananciasDomain]:
        pass
    
    @abstractmethod
    async def get_dashboard_material_by_sell(self) -> list[TipoDomain]:
        pass
    
    @abstractmethod
    async def get_dashboard_material_by_gain(self) -> list[TipoDomain]:
        pass
    
    