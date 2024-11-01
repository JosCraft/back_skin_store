from src.core.abstractions.infrastructure.repository.catematerial_repository_abstract import ICateMaterialRepository
from src.core.models.catematerial_domain import  CateMaterialDomain


class cateMaterialRepository(ICateMaterialRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[CateMaterialDomain]:
        cateMaterial = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM catematerial")
                result = cursor.fetchall()
                for row in result:
                    catematerial = CateMaterialDomain(
                        id=row["id_ct"],
                        nombre=row["nombre_ct"],
                        medida=row["medida"]
                    )
                    cateMaterial.append(catematerial)
                return cateMaterial
        except Exception as e:
            print(e)
        return cateMaterial

    async def add(self, catematerial: CateMaterialDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO catematerial (nombre_ct, medida) VALUES (%s, %s)",
                               (catematerial.nombre, catematerial.medida))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def remove(self, catematerial_id) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM catematerial WHERE id_ct = %s", (catematerial_id,))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
            return False
