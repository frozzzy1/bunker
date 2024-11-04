from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import BaseOrm


class RoomOrm(BaseOrm):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(unique=True)
    capacity: Mapped[int]
    players: Mapped[list['PlayerOrm']] = relationship(
        'PlayerOrm',
        back_populates='room',
    )
    state: Mapped[int]