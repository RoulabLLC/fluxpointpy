from .client import FluxpointClient

class sfw_gif:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def get_gif(self, image_type: str) -> dict:
        endpoint = f"/sfw/gif/{image_type}"
        return await self.client.get(endpoint)
