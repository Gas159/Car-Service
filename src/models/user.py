from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped

from models import Base
from models.mixins.int_id_pk import IntPkMixin


class User(IntPkMixin, Base):
    # __tablename__ = "users"
    # id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(unique=True)
    second_name: Mapped[str]
    email: Mapped[str | None]
    # foo: Mapped[str]
    # bar: Mapped[str]

    # __table_args__ = (UniqueConstraint("foo", "bar"),)
