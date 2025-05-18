from .client import FluxpointClient

class minecraft:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def ping_server(self, host: str, port: str = None, icon: bool = False) -> dict:
        params = {"host": host, "icon": str(icon).lower()}
        if port:
            params["port"] = port
        return await self.client.get("/mc/ping", params=params)

    async def get_uuid(self, player: str) -> dict:
        params = {"player": player}
        return await self.client.get("/mc/uuid", params=params)

    async def get_skin(self, player: str, type: str = "full") -> dict:
        params = {"player": player, "type": type}
        return await self.client.get("/mc/skin", params=params)
