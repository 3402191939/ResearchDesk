from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from backend.database import engine
from backend.models import ResearchTask
from backend.schemas import ResearchTaskCreate, ResearchTaskResponse

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
            detail="connection or query failed",
        ) from None

    return {
        "status": "ok",
        "database": "connected",
        "result": result,
    }

@app.post(
    "/tasks",
    response_model=ResearchTaskResponse,
    status_code=201,
)
def create_task(data: ResearchTaskCreate):
    task = ResearchTask(
        company=data.company,
        question=data.question,
        cutoff_date=data.cutoff_date,
    )

    try:
        with Session(engine) as session:
            session.add(task)
            session.commit()
            session.refresh(task)

            return task

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Save research task failed",
        ) from None

@app.get(
    "/tasks/{task_id}",
    response_model=ResearchTaskResponse,
)
def get_task(task_id: str):
    try:
        with Session(engine) as session:
            task = session.get(ResearchTask, task_id)

            if task is None:
                raise HTTPException(
                    status_code=404,
                    detail="Research task not found",
                )

            return task

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Failed to query research task",
        ) from None