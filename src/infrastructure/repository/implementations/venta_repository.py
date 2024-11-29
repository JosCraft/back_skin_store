from src.core.abstractions.infrastructure.repository.venta_repository_abstract import IVentaRepository
from src.core.models.venta_domain import VentaDomain


class ventaRepository(IVentaRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[VentaDomain]:
        ventas = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM venta")
                result = cursor.fetchall()
                for row in result:
                    venta = VentaDomain(
                        id=row["id_vt"],
                        fecha=row["fecha_vt"],
                        totalVenta=row["total_vt"],
                        idUsuario=row["id_usuario"],
                    )
                    ventas.append(venta)
                return ventas
        except Exception as e:
            print(e)

    async def get_by_id(self, id_sale: int) -> VentaDomain:
        venta = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM venta WHERE id_vt = %s", (id_sale,))
                result = cursor.fetchone()
                venta = VentaDomain(
                    id=result["id_vt"],
                    fecha=result["fecha_vt"],
                    totalVenta=result["total_vt"],
                    idUsuario=result["id_usuario"],
                )
                return venta
        except Exception as e:
            print(e)
        return venta

    async def create(self, ven: VentaDomain) -> int:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO venta (fecha_vt, total_vt, id_usuario) VALUES (%s, %s, %s)",
                               (ven.fecha, ven.totalVenta, ven.idUsuario))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            print(e)


