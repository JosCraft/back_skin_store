from abc import ABC, abstractmethod
from src.core.models.stats_domain import StatsDomain
from src.core.models.ventaPlot_domain import ventaPlotDomain
from src.core.models.gananciasPlot_domain import GananciasDomain
from src.core.models.tipo_domain import TipoDomain

class IDashboardRepository(ABC):

    @abstractmethod
    async def get_counts(self) -> StatsDomain:
        pass

    @abstractmethod
    async def get_ventas_plot(self) -> list[ventaPlotDomain]:
        pass
    
    @abstractmethod
    async def get_ganancias_plot(self) -> list[GananciasDomain]:
        pass
    
    @abstractmethod
    async def get_material_by_sell(self) -> list[TipoDomain]:
        pass
    
    @abstractmethod
    async def get_material_by_gain(self) -> list[TipoDomain]:
        pass
    
    