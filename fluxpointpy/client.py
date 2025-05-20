import aiohttp

class FluxpointClient:
    fluxpoint = "https://api.fluxpoint.dev"

    def __init__(self, token: str):
        self.token = token
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers={"Authorization": self.token})
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def get(self, endpoint: str, params: dict = None):
        async with self.session.get(f"{self.fluxpoint}{endpoint}", params=params) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def post(self, endpoint: str, json: dict = None):
        async with self.session.post(f"{self.fluxpoint}{endpoint}", json=json) as resp:
            resp.raise_for_status()
            return await resp.json()
