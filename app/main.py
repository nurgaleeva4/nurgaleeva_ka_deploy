from fastapi import FastAPI
from app.config import Settings
from app.routers import items
from app.logger import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

settings = Settings()
app = FastAPI(
    title=settings.app_name,
    description="Учебный проект для демонстрации тестирования и деплоя",
    version="1.0.0",
    contact={
        "name": "Kristina",
        "email": "student@example.com"
    },
)

app.include_router(items.router)

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {
        "message": "Hello, World!",
        "environment": settings.environment,
        "app_name": settings.app_name
    }

@app.get("/health")
async def health_check():
    logger.info("Health check performed")
    return {
        "status": "healthy",
        "environment": settings.environment,
        "version": "1.0.0"
    }