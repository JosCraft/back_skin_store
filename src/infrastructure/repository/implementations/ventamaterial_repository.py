from src.core.abstractions.infrastructure.repository.ventaMaterial_repository_abstract import IVentaMaterialRepository
from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.core.models.material_domain import MaterialDomain
from src.core.models.venta_domain import VentaDomain


class VentaMaterialRepository(IVentaMaterialRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[VentaMaterialDomain]:
        vendidos = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_mt, id_vt, id_tipo, id_usuario, medida_mt, fecha_vt, total_vt "
                               "FROM venta_material "
                               "INNER JOIN material ON material.id_mt = venta_material.id_venta "
                               "INNER JOIN tipo ON tipo.id_tp = material.id_tipo "
                               "INNER JOIN venta ON venta.id_vt = venta_material.id_venta")
                result = cursor.fetchall()
                print(result)
                for row in result:
                    material = MaterialDomain(
                        id=row["id_mt"],
                        medida=row["medida_mt"],
                        idTipo=row["id_tipo"],
                    )
                    venta = VentaDomain(
                        id=row["id_vt"],
                        fecha=row["fecha_vt"],
                        totalVenta=str(row["total_vt"]),
                        idUsuario=row["id_usuario"]
                    )
                    vendidos.append(VentaMaterialDomain(
                        idVenta=row["id_vt"],
                        idMaterial=row["id_mt"],
                        MaterialDomain=material,
                        VentaDomain=venta
                    ))
                return vendidos
        except Exception as e:
            print(e)
            return None

    async def get_by_id(self, id_material: int) -> VentaMaterialDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_mt, id_vt, id_tipo, id_usuario, medida_mt, fecha_vt, total_vt "
                               "FROM venta_material "
                               "INNER JOIN material ON material.id_mt = venta_material.id_venta "
                               "INNER JOIN tipo ON tipo.id_tp = material.id_mt "
                               "INNER JOIN venta ON venta.id_vt = venta_material.id_venta "
                               "WHERE id_material = %s", (id_material,))
                result = cursor.fetchone()
                material = MaterialDomain(
                    id=result["id_mt"],
                    medida=result["medida_mt"],
                    idTipo=result["id_tipo"]
                )
                venta = VentaDomain(
                    id=result["id_vt"],
                    fecha=result["fecha_vt"],
                    totalVenta=str(result["total_vt"]),
                )
                return VentaMaterialDomain(
                    idVenta=result["id_vt"],
                    idMaterial=result["id_mt"],
                    MaterialDomain=material,
                    VentaDomain=venta
                )
        except Exception as e:
            print(e)
            return None

    async def add(self, ven: VentaMaterialDomain):
        try:
            print(ven)
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("INSERT INTO venta_material (id_venta, id_material) VALUES (%s, %s)",
                               (ven.idVenta, ven.idMaterial))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def remove(self, id_material: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM venta_material WHERE id_material = %s", (id_material,))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
            return False
