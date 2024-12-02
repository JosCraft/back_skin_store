from src.core.abstractions.infrastructure.repository.ventaMaterial_repository_abstract import IVentaMaterialRepository
from src.core.models.ventaMaterial_domain import VentaMaterialDomain
from src.core.models.material_domain import MaterialDomain
from src.core.models.venta_domain import VentaDomain
from src.core.models.tipo_domain import TipoDomain

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
                        Material=material,
                        Venta=venta
                    ))
                return vendidos
        except Exception as e:
            print(e)
            return None

    async def get_by_id(self, id_material: int) -> list[VentaMaterialDomain]:
        ventaMat = []
        try:
            if not self.connection:
                raise ValueError("La conexión a la base de datos no está establecida.")
            
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM venta_material "
                    "INNER JOIN material ON material.id_mt = venta_material.id_material "
                    "INNER JOIN tipo ON tipo.id_tp = material.id_tipo "
                    "WHERE id_venta = %s", 
                    (id_material,)
                )
                result = cursor.fetchall()  # Método correcto para obtener todos los resultados.
                
                for row in result:
                    material = MaterialDomain(
                        id=row["id_mt"],
                        medida=row["medida_mt"],
                        idTipo=row["id_tipo"],
                        tipo = TipoDomain(
                        id=row["id_tp"],
                        nombre=row["nombre_tp"],
                        precio=row["precio_tp"],
                        idCategoria=row["id_categoria"],
                        idColor=row["id_color"],
                        idCurtiembre=row["id_curtiembre"]
                    )
                    )                    
                    ventaMat.append(VentaMaterialDomain(
                        idVenta=row["id_venta"],
                        idMaterial=row["id_material"],
                        Material=material
                    ))
            return ventaMat
        except Exception as e:
            print(f"Error al obtener datos por ID: {e}")
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
