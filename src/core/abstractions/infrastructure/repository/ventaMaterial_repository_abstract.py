from abc import ABC, abstractmethod
from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.core.models.ventaPlot_domain import ventaPlotDomain

class IVentaMaterialRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[VentaMaterialDomain]:
        pass

    @abstractmethod
    async def get_by_id(self, id_material: int) -> list[VentaMaterialDomain]:
        pass
    @abstractmethod
    async def get_all_for_plot(self) -> list[ventaPlotDomain]:
        pass

    @abstractmethod
    async def add(self, ven: VentaMaterialDomain):
        pass

    @abstractmethod
    async def remove(self, id_material: int) -> bool:
        pass
