from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import settings
from app.routers import contacts, health

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API FastAPI avec Pydantic, PostgreSQL et architecture en couches",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": settings.app_name}
