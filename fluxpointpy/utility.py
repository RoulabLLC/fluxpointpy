from .client import FluxpointClient

class utility:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def unix_to_date(self, unix: int, fmt: str) -> str:
        body = {"unix": unix, "format": fmt}
        data = await self.client.post("/utility/unix-date", json=body)
        return data.get("content", "")

    async def snowflake_to_date(self, snowflake: int, fmt: str) -> str:
        body = {"snowflake": snowflake, "format": fmt}
        data = await self.client.post("/utility/snowflake-date", json=body)
        return data.get("content", "")
