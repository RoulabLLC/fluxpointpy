from .client import FluxpointClient

class meme:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def get_image(self, image_type: str) -> dict:
        """Fetch a random meme image by type."""
        endpoint = f"/sfw/img/{image_type}"
        return await self.client.get(endpoint)
