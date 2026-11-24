from datetime import date, datetime
from uuid import uuid4

from sqlalchemy import Date, DateTime, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

