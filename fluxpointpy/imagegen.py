
from .client import FluxpointClient

class imagegen:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def generate(self, payload: dict) -> bytes:
        endpoint = f"{self.client.BASE_URL}/gen/custom"
        async with self.client.session.post(endpoint, json=payload) as resp:
            resp.raise_for_status()
            return await resp.read()

    async def welcome(self, payload: dict) -> bytes:
        """
        Generate a welcome image using the welcome endpoint.
        """
        endpoint = f"{self.client.BASE_URL}/gen/welcome"
        async with self.client.session.post(endpoint, json=payload) as resp:
            resp.raise_for_status()
            return await resp.read()
