from src.core.abstractions.infrastructure.repository.curtiembre_repository_abstract import ICurtiembreRepository
from src.core.models.curtiembre_domain import CurtiembreDomain


class CurtiembreRepository(ICurtiembreRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[CurtiembreDomain]:
        curtiembres = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM curtiembre")
                result = cursor.fetchall()
                print(result)
                for row in result:
                    curt = CurtiembreDomain(
                        id=row["id_cr"],
                        nombre=row["nombre_cr"],
                        numero=row["numero_cr"],
                    )
                    curtiembres.append(curt)
                return curtiembres
        except Exception as e:
            print(e)
        return curtiembres

    async def get_by_id(self, id_curtiembre: int) -> CurtiembreDomain:
        curt = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM curtiembre WHERE id_cr = %s", (id_curtiembre,))
                result = cursor.fetchone()
                curt = CurtiembreDomain(
                    id=result["id_cr"],
                    nombre=result["nombre_cr"],
                    numero=result["numero_cr"],
                )
                return curt
        except Exception as e:
            print(e)
        return curt

    async def create(self, curt: CurtiembreDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO curtiembre (nombre_cr, numero_cr) VALUES (%s, %s)",
                               (curt.nombre, curt.numero))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def update(self, id_curtiembre: int, curt: CurtiembreDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE curtiembre SET nombre_cr = %s, numero_cr = %s WHERE id_cr = %s",
                               (curt.nombre, curt.numero, id_curtiembre))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def delete(self, id_curtiembre: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM curtiembre WHERE id_cr = %s", (id_curtiembre,))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
        return False
