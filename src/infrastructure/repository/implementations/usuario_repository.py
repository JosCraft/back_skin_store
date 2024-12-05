from src.core.abstractions.infrastructure.repository.usuario_repository_abstract import IUsuarioRepository
from src.core.models.usuario_domain import UsuarioDomain
import bcrypt

class usuarioRepository(IUsuarioRepository):
    
    def __init__(self, connection):
        self.connection = connection
        print("UsuarioRepository")

    async def get_all(self) -> list[UsuarioDomain]:
        usuarios = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_usr, nombre_usr, ape_usr, numero_usr, email, activo, role FROM usuario")
                results = cursor.fetchall()
                for row in results:
                    usuarios.append(UsuarioDomain(
                        id=row['id_usr'],
                        nombre=row['nombre_usr'],
                        apelldio=row['ape_usr'],
                        numero=row['numero_usr'],
                        email=row['email'],
                        activo=row['activo'],
                        role=row['role']
                        
                    ))
        except Exception as e:
            print(e)
        return usuarios

    async def get_by_id(self, id_usr: int) -> UsuarioDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id_usr, nombre_usr, ape_usr, numero_usr, email, activo, role FROM usuario WHERE id_usr = %s", (id_usr,))
                user_row = cursor.fetchone()
                if not user_row:
                    return None
                return UsuarioDomain(
                    id=user_row['id_usr'],
                    nombre=user_row['nombre_usr'],
                    apelldio=user_row['ape_usr'],
                    numero=user_row['numero_usr'],
                    email=user_row['email'],
                    activo=user_row['activo'],
                    role=user_row['role']
                )
        except Exception as e:
            print(e)
        return None

    async def register(self, usr: UsuarioDomain):
        try:
            with self.connection.cursor() as cursor:            
                hashed_password = bcrypt.hashpw(usr.password.encode('utf-8'), bcrypt.gensalt())
                        
                cursor.execute(" INSERT INTO usuario (nombre_usr, ape_usr, numero_usr, email, password, activo, role) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    usr.nombre,
                    usr.apelldio,
                    usr.numero,
                    usr.email,
                    hashed_password.decode('utf-8'),
                    usr.activo,
                    usr.role,
                ))
                
                self.connection.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    async def login(self, email: str, passwordLg: str) -> UsuarioDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                # Buscar usuario por email                
                print(cursor)
                cursor.execute("SELECT id_usr, nombre_usr, ape_usr, numero_usr, email, password, activo, role FROM usuario WHERE email = %s", (email,))
                user_row = cursor.fetchone()
                if not user_row:
                    return None
                if not user_row['activo']:
                    return None

                if not bcrypt.checkpw(passwordLg.encode('utf-8'), user_row['password'].encode('utf-8')):
                    return None  

                return UsuarioDomain(
                    id=user_row['id_usr'],
                    nombre=user_row['nombre_usr'],
                    apelldio=user_row['ape_usr'],
                    numero=user_row['numero_usr'],
                    password='',
                    email=email,
                    activo=user_row['activo'],
                    role=user_row['role']
                )
        except Exception as e:
            print(f"Error durante el login: {e}")
            return None
        
    async def update(self, id_usr: int, usr: UsuarioDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE usuario SET nombre_usr = %s, ape_usr = %s, numero_usr = %s, email = %s, activo = %s, role = %s WHERE id_usr = %s", (
                    usr.nombre,
                    usr.apelldio,
                    usr.numero,
                    usr.email,
                    usr.activo,
                    usr.role,
                    id_usr
                ))
                self.connection.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    async def delete(self, id_usr: int) -> bool:
        try:
            # Primero, actualizamos los registros en la tabla "venta" para desvincular al usuario
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE venta SET id_usuario = NULL WHERE id_usuario = %s", (id_usr,)
                )
                self.connection.commit()
            
            # Luego, eliminamos el registro del usuario en la tabla "usuario"
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuario WHERE id_usr = %s", (id_usr,))
                self.connection.commit()

            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
