from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthStateSchema
from app.database.models.health import HealthStateOrm


class HealthStateRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: AddHealthStateSchema) -> None:
        health = HealthStateOrm(**data.model_dump())
        self.session.add(health)
        await self.session.commit()

    async def get_all_health_states(self) -> HealthStateOrm:
        query = select(HealthStateOrm)
        result = await self.session.scalars(query)
        return result
