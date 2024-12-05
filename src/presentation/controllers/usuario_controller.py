import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.core.abstractions.services.usuario_service_abstract import IUsuarioService
from src.core.dependency_inyection.dependency_inyection import build_usuario_service
from src.presentation.dto.usuario_dto import UsuarioDTO
from src.presentation.mappers.map_dto_domain_usuario import map_domain_dto_to_usuario

SECRET_KEY = "XrkLgy5qnB"  
ALGORITHM = "HS256"

usuario_controller = APIRouter(prefix="/api/v1", tags=["usuario"])

def generar_token(usuario_id: int, role: str) -> str:
    print(usuario_id, role)  # Debug print to check the type
    payload = {
        "sub": str(usuario_id),  # Convert to string to avoid the error
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)



security = HTTPBearer()

def verificar_token_y_rol(
    credentials: HTTPAuthorizationCredentials = Security(security),
    rol_permitido: str = None
):
    try:
        try:
            payload = jwt.decode(str(credentials.credentials), SECRET_KEY, algorithms=[ALGORITHM])
            print("Decoded payload:", payload)
            print("Token decoded successfully.")
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="El token ha expirado."
            )
        except jwt.InvalidTokenError as e:
            print(f"Invalid token error: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido."
            )
        # Get the role from the payload
        rol_usuario = payload.get("role")
        
        # Check if the role matches the permitted role
        if rol_permitido and rol_usuario != rol_permitido:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permiso para acceder a esta ruta."
            )

        return payload  # Return the payload if the token is valid and the role matches

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token ha expirado."
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido."
        )


@usuario_controller.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    usuario_dto: UsuarioDTO, 
    usuario_service: IUsuarioService = Depends(build_usuario_service)
):
    try:
        print(usuario_dto)
        usuario_domain = map_domain_dto_to_usuario(usuario_dto)
        print(usuario_domain)
        registrado = await usuario_service.register_usuario(usuario_domain)
        
        if not registrado:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El usuario ya existe o no pudo ser registrado."
            )
        
        return {"message": "Usuario registrado exitosamente"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@usuario_controller.post("/login", status_code=status.HTTP_200_OK)
async def login_user(
    email: str,
    password: str,
    usuario_service: IUsuarioService = Depends(build_usuario_service)
):
    print(email, password)
    usuario = await usuario_service.login_usuario(email, password)
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas o usuario inactivo."
        )
    

    token = generar_token(usuario.id, usuario.role)
    
    return {
        "message": "Login exitoso",
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "role": usuario.role
        },
        "token": token 
    }



@usuario_controller.get("/perfil", dependencies=[Depends(verificar_token_y_rol)])
async def perfil(payload: dict = Depends(verificar_token_y_rol)):
    return {"message": "Acceso permitido", "usuario": payload}


@usuario_controller.get("/admin", dependencies=[Depends(lambda cred: verificar_token_y_rol(cred, rol_permitido="ADMIN"))])
async def admin_ruta(payload: dict = Depends(verificar_token_y_rol)):
    return {"message": "Acceso permitido", "usuario": payload}


@usuario_controller.get("/user")
async def get_all(usuario_service: IUsuarioService = Depends(build_usuario_service)):
    try:
        usuarios = await usuario_service.get_all_usuario()
        return usuarios
    except Exception as e:
        return {"error": str(e)}

@usuario_controller.get("/user/{usuario_id}")
async def get_by_id(usuario_id: int, usuario_service: IUsuarioService = Depends(build_usuario_service)):
    try:
        usuario = await usuario_service.get_usuario_by_id(usuario_id)
        return usuario
    except Exception as e:
        return {"error": str(e)}
    
@usuario_controller.put("/user/{usuario_id}")
async def update_usuario(usuario_id: int, usuario_dto: UsuarioDTO, usuario_service: IUsuarioService = Depends(build_usuario_service)):
    try:
        print(usuario_id, usuario_dto)

        # Mapeo del DTO al dominio
        usuario = map_domain_dto_to_usuario(usuario_dto)
        print(usuario)

        # Actualización del usuario en el servicio
        await usuario_service.update_usuario(usuario_id, usuario)
        return {"message": "Usuario actualizado correctamente"}

    except RequestValidationError as ve:
        # Si la validación del esquema falla, devolvemos un detalle claro
        return JSONResponse(
            status_code=422,
            content={"error": "Datos inválidos", "detalles": ve.errors()},
        )

    except HTTPException as he:
        # Si se lanza una excepción HTTP, devolvemos la misma
        return JSONResponse(
            status_code=he.status_code,
            content={"error": he.detail},
        )

    except Exception as e:
        # Manejamos errores genéricos
        return {"error": f"Error inesperado: {str(e)}"}



@usuario_controller.delete("/user/{usuario_id}")
async def delete_usuario(usuario_id: int, usuario_service: IUsuarioService = Depends(build_usuario_service)):
    try:
        await usuario_service.delete_usuario(usuario_id)
        return {"message": "Usuario eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}