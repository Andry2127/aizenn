from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.models.base import Base

class Position(Base):
    __tablename__ = "position"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


