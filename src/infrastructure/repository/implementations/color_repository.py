from src.core.abstractions.infrastructure.repository.color_repository_abstract import IColorRepository
from src.core.models.color_domain import ColorDomain


class colorRepository(IColorRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[ColorDomain]:
        colores = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM color")
                result = cursor.fetchall()
                for row in result:
                    color = ColorDomain(
                        id=row["id_cl"],
                        nombre=row["nombre_cl"],
                        codigoHex=row["codigo_hx"]
                    )
                    colores.append(color)
                return colores
        except Exception as e:
            print(e)
        return colores

    async def get_by_id(self, color_id) -> ColorDomain:
        color = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM color WHERE id_cl = %s", (color_id,))
                result = cursor.fetchone()
                color = ColorDomain(
                    id=result["id_cl"],
                    nombre=result["nombre_cl"],
                    codigoHex=result["codigo_hx"]
                )
                return color
        except Exception as e:
            print(e)
        return color

    async def create(self, color: ColorDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO color (nombre_cl, codigo_hx) VALUES (%s, %s)",
                               (color.nombre, color.codigoHex))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def update(self, color_id: int, color: ColorDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE color SET nombre_cl = %s, codigo_hx = %s WHERE id = %s",
                               (color.nombre, color.codigoHex, color_id))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def delete(self, color_id) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM color WHERE id_cl = %s", (color_id,))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
            return False
