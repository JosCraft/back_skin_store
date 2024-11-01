from src.core.abstractions.infrastructure.repository.tipo_repository_abstract import ITipoRepository
from src.core.models.tipo_domain import TipoDomain
from src.core.models.color_domain import ColorDomain
from src.core.models.curtiembre_domain import CurtiembreDomain


class tipoRepository(ITipoRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all(self) -> list[TipoDomain]:
        tipos = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_tp, nombre_tp, precio_tp, id_color, id_curtiembre, id_categoria , "
                               "nombre_cl, codigo_hx, "
                               "nombre_cr, numero_cr "
                               "FROM tipo "
                               "INNER JOIN color ON tipo.id_color = color.id_cl "
                               "INNER JOIN curtiembre ON tipo.id_curtiembre = curtiembre.id_cr")
                result = cursor.fetchall()
                for row in result:
                    color = ColorDomain(
                        id=row["id_color"],
                        nombre=row["nombre_cl"],
                        codigoHex=row["codigo_hx"]
                    )
                    curtiembre = CurtiembreDomain(
                        id=row["id_curtiembre"],
                        nombre=row["nombre_cr"],
                        numero=row["numero_cr"]
                    )
                    tip = TipoDomain(
                        id=row["id_tp"],
                        nombre=row["nombre_tp"],
                        precio=row["precio_tp"],
                        idCategoria=row["id_categoria"],
                        idColor=row["id_color"],
                        idCurtiembre=row["id_curtiembre"],
                        color=color,
                        curtiembre=curtiembre
                    )
                    tipos.append(tip)
                return tipos
        except Exception as e:
            print(e)
        return tipos

    async def get_by_id(self, id_tipo: int) -> TipoDomain:
        tip = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_tp, id_categoria ,nombre_tp, precio_tp, id_color, id_curtiembre, "
                               "nombre_cl, codigo_hx, "
                               "nombre_cr, numero_cr "
                               "FROM tipo "
                               "INNER JOIN color ON tipo.id_color = color.id_cl "
                               "INNER JOIN curtiembre ON tipo.id_curtiembre = curtiembre.id_cr  "
                               "WHERE tipo.id_tp = %s", (id_tipo,))
                result = cursor.fetchone()
                color = ColorDomain(
                    id=result["id_color"],
                    nombre=result["nombre_cl"],
                    codigoHex=result["codigo_hx"]
                )
                curtiembre = CurtiembreDomain(
                    id=result["id_curtiembre"],
                    nombre=result["nombre_cr"],
                    numero=result["numero_cr"]
                )
                tip = TipoDomain(
                    id=result["id_tp"],
                    nombre=result["nombre_tp"],
                    precio=result["precio_tp"],
                    idCategoria=result["id_categoria"],
                    idColor=result["id_color"],
                    idCurtiembre=result["id_curtiembre"],
                    color=color,
                    curtiembre=curtiembre
                )
                return tip
        except Exception as e:
            print(e)
        return tip

    async def create(self, tip: TipoDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tipo (nombre_tp, precio_tp, id_categoria,id_color, id_curtiembre)"
                    " VALUES (%s, %s, %s, %s, %s)",
                    (tip.nombre, tip.precio, tip.idCategoria, tip.idColor, tip.idCurtiembre))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def update(self, id_tipo: int, tip: TipoDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE tipo "
                    "SET nombre_tp = %s, precio_tp = %s, id_categoria = %s, id_color = %s, id_curtiembre = %s"
                    " WHERE id_tp = %s",
                    (tip.nombre, tip.precio, tip.idCategoria, tip.idColor, tip.idCurtiembre, id_tipo))
                self.connection.commit()
        except Exception as e:
            print(e)

    async def delete(self, id_tipo: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM tipo WHERE id_tp = %s", (id_tipo,))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
            return False
