from .client import FluxpointClient
class misc:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def get_dad_joke(self) -> str:
        data = await self.client.get("/dadjoke")
        return data.get("joke", "")

    async def get_user_info(self) -> dict:
        return await self.client.get("/me")
