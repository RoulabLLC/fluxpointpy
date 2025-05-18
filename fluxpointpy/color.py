from .client import FluxpointClient

class color:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def get_random_color(self) -> dict:
        return await self.client.get("/color/random")

    async def get_color_info(self, query: str) -> dict:
        params = {"name": query}
        return await self.client.get("/color/info", params=params)
