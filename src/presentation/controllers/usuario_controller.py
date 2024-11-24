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
    payload = {
        "sub": usuario_id,
        "role": role, 
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


security = HTTPBearer()

def verificar_token_y_rol(
    credentials: HTTPAuthorizationCredentials = Security(security), 
    roles_permitidos: list[str] = None
):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        
        if roles_permitidos:
            rol_usuario = payload.get("role")
            if rol_usuario not in roles_permitidos:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="No tienes permiso para acceder a esta ruta."
                )
        
        return payload  
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

@usuario_controller.get("/admin", dependencies=[Depends(verificar_token_y_rol)])
async def admin_ruta(payload: dict = Depends(lambda cred: verificar_token_y_rol(cred, roles_permitidos=["ADMIN"]))):
    return {"message": "Acceso no permitido", "usuario": payload}
