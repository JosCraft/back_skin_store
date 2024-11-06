from src.core.abstractions.infrastructure.repository.inventario_repository_abstract import IInventarioRepository
from src.core.models.inventario_domain import InventarioDomain
from src.core.models.material_domain import MaterialDomain
from src.core.models.tipo_domain import TipoDomain
from src.core.models.color_domain import ColorDomain
from src.core.models.curtiembre_domain import CurtiembreDomain

class InventarioRepository(IInventarioRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[MaterialDomain]:
        inventarios = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM inventario "
                               "INNER JOIN material ON material.id_mt = inventario.id_material "
                               "INNER JOIN tipo ON tipo.id_tp = material.id_tipo "
                               "INNER JOIN color ON tipo.id_color = color.id_cl "
                               "INNER JOIN curtiembre ON tipo.id_curtiembre = curtiembre.id_cr")
                result = cursor.fetchall()
                for row in result:
                    color = ColorDomain(
                        id=row["id_color"],  # Changed result to row
                        nombre=row["nombre_cl"],
                        codigoHex=row["codigo_hx"],
                    )
                    curtiembre = CurtiembreDomain(
                        id=row["id_curtiembre"],
                        nombre=row["nombre_cr"],
                        numero=row["numero_cr"],
                    )
                    tipo = TipoDomain(
                        id=row["id_tp"],
                        nombre=row["nombre_tp"],
                        precio=row["precio_tp"],
                        idCategoria=row["id_categoria"],
                        idColor=row["id_color"],
                        idCurtiembre=row["id_curtiembre"],
                        color=color,
                        curtiembre=curtiembre,
                    )
                    inv = MaterialDomain(
                        id=row["id_material"],
                        medida=row["medida_mt"],
                        idTipo=row["id_tipo"],
                        tipo=tipo,
                    )
                    inventarios.append(inv)
            return inventarios
        except Exception as e:
            print(e)
        return inventarios

    async def get_by_id(self, id_inv: int) -> MaterialDomain:
        inv = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM inventario "
                               "INNER JOIN material ON material.id_mt = inventario.id_material "
                               "INNER JOIN tipo ON tipo.id_tp = material.id_tipo "  # Fixed id_tipo to match material
                               "WHERE id_inv = %s", (id_inv,))
                result = cursor.fetchone()
                if result:
                    tipo = TipoDomain(
                        id=result["id_tp"],
                        nombre=result["nombre_tp"],
                        precio=result["precio_tp"],
                        idCategoria=result["id_categoria"],
                        idColor=result["id_color"],
                        idCurtiembre=result["id_curtiembre"]
                    )
                    inv = MaterialDomain(
                        id=result["id_mt"],
                        medida=result["medida_mt"],
                        idTipo=result["id_tipo"],
                        tipo=tipo,
                    )
            return inv
        except Exception as e:
            print(e)
        return inv

    async def add(self, inv: InventarioDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO inventario (id_material) VALUES (%s)",
                               (inv.idMaterial,))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def remove(self, id_inv: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM inventario WHERE id_inv = %s", (id_inv,))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
        return False
