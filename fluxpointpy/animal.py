
from .client import FluxpointClient

class animal:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def _get_animal_image(self, animal: str) -> str:
        endpoint = f"/sfw/img/{animal}"
        data = await self.client.get(endpoint)
        return data.get("file", "")

    async def cat(self) -> str:
        return await self._get_animal_image("cat")

    async def dog(self) -> str:
        return await self._get_animal_image("dog")

    async def duck(self) -> str:
        return await self._get_animal_image("duck")

    async def lizard(self) -> str:
        return await self._get_animal_image("lizard")

