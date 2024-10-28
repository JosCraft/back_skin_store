from src.core.abstractions.infrastructure.repository.material_repository_abstract import IMaterialRepository
from src.core.models.material_domain import MaterialDomain


class MaterialRepository(IMaterialRepository):

    def __init__(self,connection):
        self.connection = connection

    def get_all_by_tipo(self, id_tipo: int) -> list[MaterialDomain]:
        materiales = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * "
                               "FROM material "
                               "WHERE material.id_tipo = %s", (id_tipo,))
                result = cursor.fetchall()
                for row in result:
                    mat = MaterialDomain(
                        id=row["id_mt"],
                        medida=row["medida_mt"],
                        idTipo=row["id_tipo"]
                    )
                    materiales.append(mat)
        except Exception as e:
            print(e)
        return materiales

    def get_by_id(self, id_material: int) -> MaterialDomain:
        mat = None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM material WHERE id = %s", (id_material,))
                result = cursor.fetchone()
                mat = MaterialDomain(
                    id=result["id_mt"],
                    medida=result["medida_mt"],
                    idTipo=result["id_tipo"]
                )
        except Exception as e:
            print(e)
        return mat

    def create(self, mat: MaterialDomain) -> MaterialDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO material (medida_mt, id_tipo) VALUES (%s, %s)",
                               (mat.medida, mat.idTipo))
                self.connection.commit()
        except Exception as e:
            print(e)
        return mat

    def update(self, id_material: int, mat: MaterialDomain) -> MaterialDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE material SET medida_mt = %s, id_tipo = %s WHERE id = %s",
                               (mat.medida, mat.idTipo, id_material))
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