from datetime import date, datetime
from uuid import uuid4

from sqlalchemy import Date, DateTime, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class ResearchTask(Base):
    __tablename__ = "research_tasks"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    company: Mapped[str] = mapped_column(String(100))

    question: Mapped[str] = mapped_column(Text)

    cutoff_date: Mapped[date] = mapped_column(Date)

    status: Mapped[str] = mapped_column(
        String(30),
        default="created",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )