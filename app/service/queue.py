import httpx

from app.settings import get_settings
from app.schemas.solution import SolutionSchema


class QueueInterface:
     @staticmethod
     async def add_solutiion(solution: SolutionSchema):
        return httpx.post(
            get_settings().get_queue_url(),
            data=solution.dict()
        )
