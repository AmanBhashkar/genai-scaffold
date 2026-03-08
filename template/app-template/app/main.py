from fastapi import FastAPI
from app.api.v1 import router as api_v1_router
from app.core.config import settings
from app.core.db import init_db

app = FastAPI(
    title="{{ project_name }}",
    description="{{ description }}",
    version="0.1.0",
)

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(api_v1_router.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
