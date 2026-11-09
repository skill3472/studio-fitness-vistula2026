from datetime import UTC, datetime

from sqlalchemy.orm import Mapped, mapped_column

from common.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    username: Mapped[str] = mapped_column(index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), nullable=False
    )
