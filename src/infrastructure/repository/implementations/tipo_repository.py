from src.core.abstractions.infrastructure.repository.tipo_repository_abstract import ITipoRepository
from src.core.models.tipo_domain import TipoDomain

class tipoRepository(ITipoRepository):

    def __init__(self, connection):
        self.connection = connection
    def get_all(self) -> list[TipoDomain]:
        tipos = []
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM tipo")
                result = cursor.fetchall()
                for row in result:
                    tip = TipoDomain(
                        id=row["id"],
                        nombre=row["nombre"],
                        descripcion=row["descripcion"]
                    )
                    tipos.append(tip)
        except Exception as e:
            print(e)
        return tipos

    def get_by_id(self, id: int) -> TipoDomain:
        tip = None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM tipo WHERE id = %s", (id,))
                result = cursor.fetchone()
                tip = TipoDomain(
                    id=result["id"],
                    nombre=result["nombre"],
                    descripcion=result["descripcion"]
                )
        except Exception as e:
            print(e)
        return tip

    def create(self, tip: TipoDomain) -> TipoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO tipo (nombre, descripcion) VALUES (%s, %s)",
                               (tip.nombre, tip.descripcion))
                self.connection.commit()
        except Exception as e:
            print(e)
        return tip

    def update(self, id: int, tip: TipoDomain) -> TipoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE tipo SET nombre = %s, descripcion = %s WHERE id = %s",
                               (tip.nombre, tip.descripcion, id))
                self.connection.commit()
        except Exception as e:
            print(e)
        return tip

    def delete(self, id: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM tipo WHERE id = %s", (id,))
                self.connection.commit()
        except Exception as e:
            print(e)
        return True