from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from backend.database import engine

app = FastAPI(title="ResearchDesk")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
def database_health():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT 1")
            ).scalar_one()

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="数据库连接或查询失败",
        ) from None

    return {
        "status": "ok",
        "database": "connected",
        "result": result,
    }