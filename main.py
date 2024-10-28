import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.presentation.controllers.color_controller import color_controller
from src.presentation.controllers.curtiembre_controller import curtiembre_controller
from src.presentation.controllers.tipo_controller import tipo_controller

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(curtiembre_controller)
app.include_router(color_controller)
app.include_router(tipo_controller)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000,log_level="debug")