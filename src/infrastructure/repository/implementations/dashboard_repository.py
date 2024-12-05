from src.core.abstractions.infrastructure.repository.dahsboard_repository_abstract import *


class DashboardRepository(IDashboardRepository):
    
    def __init__(self,connection):
        self.connection = connection
        
     
    async def get_counts(self) -> StatsDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                    SELECT 
                        (SELECT COUNT(*) FROM USUARIO WHERE activo = 1) AS cant_users,
                        (SELECT COUNT(*) FROM MATERIAL) AS cant_material,
                        (SELECT SUM(total_vt) FROM VENTA) AS cant_ganancias,
                        (SELECT COUNT(*) FROM VENTA) AS cant_ventas;
                """)
                result = cursor.fetchone()
                return StatsDomain(**result)
        except Exception as e:
            print(e)
            return StatsDomain(cant_users=0, cant_material=0, cant_ganancias=0, cant_ventas=0)

    async def get_ventas_plot(self) -> list[ventaPlotDomain]:
        ventas_plot = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                    SELECT 
                        TIPO.nombre_tp AS tipoMaterial,
                        COUNT(VENTA_MATERIAL.id_material) AS totalVentas,
                        SUM(VENTA.total_vt) AS totalIngresos
                    FROM VENTA_MATERIAL
                    JOIN VENTA ON VENTA.id_vt = VENTA_MATERIAL.id_venta
                    JOIN MATERIAL ON MATERIAL.id_mt = VENTA_MATERIAL.id_material
                    JOIN TIPO ON TIPO.id_tp = MATERIAL.id_tipo
                    GROUP BY TIPO.nombre_tp;
                """)
                results = cursor.fetchall()
                for row in results:
                    ventas_plot.append(ventaPlotDomain(**row))
        except Exception as e:
            print(e)
        return ventas_plot

    async def get_ganancias_plot(self) -> list[GananciasDomain]:
        ganancias = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                    SELECT 
                        VENTA.fecha_vt AS fecha,
                        SUM(VENTA.total_vt) AS ganancia
                    FROM VENTA
                    GROUP BY VENTA.fecha_vt
                    ORDER BY VENTA.fecha_vt;
                """)
                results = cursor.fetchall()
                for row in results:
                    ganancias.append(GananciasDomain(**row))
        except Exception as e:
            print(e)
        return ganancias

    async def get_material_by_sell(self) -> list[TipoDomain]:
        materiales = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                    SELECT 
                        tipo.id_tp AS id,
                        TIPO.nombre_tp AS tipo,
                        COUNT(VENTA_MATERIAL.id_material) AS totalVentas
                    FROM VENTA_MATERIAL
                    JOIN MATERIAL ON MATERIAL.id_mt = VENTA_MATERIAL.id_material
                    JOIN TIPO ON TIPO.id_tp = MATERIAL.id_tipo
                    GROUP BY  TIPO.nombre_tp
                    ORDER BY totalVentas DESC;
                """)
                results = cursor.fetchall()
                cont = 0
                for row in results:
                    tipo = TipoDomain(
                        id=row["id"],
                        nombre=row["tipo"],
                        cantVentas=row["totalVentas"]
                    )
                    materiales.append(tipo)
        except Exception as e:
            print(e)
        return materiales

    async def get_material_by_gain(self) -> list[TipoDomain]:
        materiales = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                    SELECT 
                        tipo.id_tp AS id,
                        TIPO.nombre_tp AS tipo,
                        SUM(VENTA.total_vt) AS totalGanancias
                    FROM VENTA_MATERIAL
                    JOIN MATERIAL ON MATERIAL.id_mt = VENTA_MATERIAL.id_material
                    JOIN VENTA ON VENTA.id_vt = VENTA_MATERIAL.id_venta
                    JOIN TIPO ON TIPO.id_tp = MATERIAL.id_tipo
                    GROUP BY TIPO.nombre_tp
                    ORDER BY totalGanancias DESC;
                """)
                results = cursor.fetchall()
                for row in results:                    
                    materiales.append(TipoDomain(
                        id=row["id"],
                        nombre=row["tipo"],
                        ganancias=row["totalGanancias"]
                    ))
        except Exception as e:
            print(e)
        return materiales

        