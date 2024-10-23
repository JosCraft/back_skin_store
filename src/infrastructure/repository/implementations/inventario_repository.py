from src.core.abstractions.infrastructure.repository.inventario_repository_abstract import IInventarioRepository
from src.core.models.inventario_domain import InventarioDomain
from src.core.models.material_domain import MaterialDomain
from src.core.models.tipo_domain import TipoDomain


class InventarioRepository(IInventarioRepository):

    def __init__(self, connection):
        self.connection = connection

    def get_all(self) -> list[MaterialDomain]:
        inventarios = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM material join inventario on material.id_mt = inventario.id_material")
                result = cursor.fetchall()
                for row in result:
                    cursor.execute("SELECT * FROM tipo WHERE id_tp = %s", (row["id_tipo"],))
                    tipo = cursor.fetchone()
                    cursor.execute("SELECT * FROM color WHERE id_cl = %s", (tipo["id_color"],))
                    color = cursor.fetchone()
                    cursor.execute("SELECT * FROM curtiembre WHERE id_cr = %s", (tipo["id_curtiembre"],))
                    curtiembre = cursor.fetchone()
                    inv = MaterialDomain(
                        id_mt=row["id_mt"],
                        medida=row["medida_mt"],
                        tipo=TipoDomain(
                            id_tp=tipo["id_tp"],
                            nombre=tipo["nombre_tp"],
                            precio=tipo["precio_tp"],
                            Color=color["nombre_cl"],
                            Curtiembre=curtiembre
                        )
                    )
                    inventarios.append(inv)
        except Exception as e:
            print(e)
        return inventarios

    def get_by_id(self, id: int) -> MaterialDomain:
        inv = None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM inventario WHERE idInventario = %s", (id,))
                result = cursor.fetchone()
                inv = InventarioDomain(
                    idInventario=result["idInventario"],
                    idMaterial=result["idMaterial"]
                )
        except Exception as e:
            print(e)
        return inv

    def create(self, inv: InventarioDomain) -> InventarioDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO inventario (idMaterial) VALUES (%s)",
                               (inv.idMaterial))
                self.connection.commit()
        except Exception as e:
            print(e)
        return inv

    def update(self, id: int, inv: InventarioDomain) -> InventarioDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE inventario SET idMaterial = %s WHERE idInventario = %s",
                               (inv.idMaterial, id))
                self.connection.commit()
        except Exception as e:
            print(e)
        return inv

    def delete(self, id: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM inventario WHERE idInventario = %s", (id,))
                self.connection.commit()
        except Exception as e:
            print(e)
        return True
