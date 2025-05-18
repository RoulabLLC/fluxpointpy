from .client import FluxpointClient

class sfw_image:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def get_image(self, image_type: str) -> dict:
        endpoint = f"/sfw/img/{image_type}"
        return await self.client.get(endpoint)
