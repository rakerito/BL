from fastapi import FastAPI
from app.routes import rutas
from app.routes.disponibilidad_routes import router as disponibilidad_router

app = FastAPI()

app.include_router(rutas.router)
app.include_router(disponibilidad_router, prefix="/api/v1", tags=["Disponibilidad"])
# .\venv\Scripts\activate
# uvicorn app.main:app --reload
#deactivate
#pip freeze > requirements.txt
