from .client import FluxpointClient

class list:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def templates(self) -> list[str]:
        data = await self.client.get("/list/templates")
        return data.get("list", [])

    async def banners(self) -> list[str]:
        data = await self.client.get("/list/banners")
        return data.get("list", [])

    async def icons(self) -> list[str]:
        data = await self.client.get("/list/icons")
        return data.get("list", [])

    async def fonts(self) -> list[str]:
        data = await self.client.get("/list/fonts")
        return data.get("list", [])
