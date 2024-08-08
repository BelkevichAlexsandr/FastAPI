import datetime

from sqlalchemy import (
    ForeignKey,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.databases.connect import Base


class BaseClass:
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    deleted_at: Mapped[datetime.datetime | None]
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        default=func.now(),
        onupdate=func.current_timestamp(),
    )


class First(BaseClass, Base):
    __tablename__ = "first"

    name: Mapped[str | None]
    last_name: Mapped[str]
    date: Mapped[datetime.datetime]

    seconds: Mapped["Second"] = relationship(back_populates="first")


class Second(BaseClass, Base):
    __tablename__ = "second"

    second_id: Mapped[int] = mapped_column(ForeignKey("first.id"))
    year: Mapped[str]

    first: Mapped["First"] = relationship(back_populates="second")
