from src.core.abstractions.infrastructure.repository.tipo_repository_abstract import ITipoRepository
from src.core.models.tipo_domain import TipoDomain
from src.core.models.color_domain import ColorDomain
from src.core.models.curtiembre_domain import CurtiembreDomain


class tipoRepository(ITipoRepository):

    def __init__(self, connection):
        self.connection = connection

    def get_all(self) -> list[TipoDomain]:
        tipos = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_tp, nombre_tp, precio_tp,tipo_medida, id_color, id_curtiembre, "
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
                        medida=row["tipo_medida"],
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

    def get_by_id(self, id_tipo: int) -> TipoDomain:
        tip = None
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_tp, nombre_tp, precio_tp,tipo_medida, id_color, id_curtiembre, "
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
                    medida=result["tipo_medida"],
                    idColor=result["id_color"],
                    idCurtiembre=result["id_curtiembre"],
                    color=color,
                    curtiembre=curtiembre
                )
                return tip
        except Exception as e:
            print(e)
        return tip

    def create(self, tip: TipoDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tipo (nombre_tp, precio_tp, tipo_medida, id_color, id_curtiembre)"
                    " VALUES (%s, %s, %s, %s, %s)",
                    (tip.nombre, tip.precio, tip.medida, tip.idColor, tip.idCurtiembre))
                self.connection.commit()
        except Exception as e:
            print(e)

    def update(self, id_tipo: int, tip: TipoDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE tipo "
                    "SET nombre_tp = %s, precio_tp = %s, tipo_medida = %s, id_color = %s, id_curtiembre = %s"
                    " WHERE id_tp = %s",
                    (tip.nombre, tip.precio, tip.medida, tip.idColor, tip.idCurtiembre, id_tipo))
                self.connection.commit()
        except Exception as e:
            print(e)

    def delete(self, id_tipo: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM tipo WHERE id_tp = %s", (id_tipo,))
                self.connection.commit()
                return True
        except Exception as e:
            print(e)
            return False
