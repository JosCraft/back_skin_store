from src.core.abstractions.infrastructure.repository.material_repository_abstract import IMaterialRepository
from src.core.models.material_domain import MaterialDomain

class MaterialRepository(IMaterialRepository):

    def __init__(self,connection):
        self.connection = connection
    def get_all(self) -> list[MaterialDomain]:
        materiales = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM material")
                result = cursor.fetchall()
                for row in result:
                    mat = MaterialDomain(
                        id=row["id"],
                        nombre=row["nombre"],
                        precio=row["precio"]
                    )
                    materiales.append(mat)
        except Exception as e:
            print(e)
        return materiales

    def get_by_id(self, id: int) -> MaterialDomain:
        mat = None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM material WHERE id = %s", (id,))
                result = cursor.fetchone()
                mat = MaterialDomain(
                    id=result["id"],
                    nombre=result["nombre"],
                    precio=result["precio"]
                )
        except Exception as e:
            print(e)
        return mat

    def create(self, mat: MaterialDomain) -> MaterialDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO material (nombre, precio) VALUES (%s, %s)",
                               (mat.nombre, mat.precio))
                self.connection.commit()
        except Exception as e:
            print(e)
        return mat

    def update(self, id: int, mat: MaterialDomain) -> MaterialDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE material SET nombre = %s, precio = %s WHERE id = %s",
                               (mat.nombre, mat.precio, id))
                self.connection.commit()
        except Exception as e:
            print(e)
        return mat

    def delete(self, id: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM material WHERE id = %s", (id,))
                self.connection.commit()
        except Exception as e:
            print(e)
        return True