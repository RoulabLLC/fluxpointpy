# file: nsfw_gif.py

from .client import FluxpointClient

class nsfwgifs:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def _get_nsfw_gif(self, category: str) -> str:
        endpoint = f"/nsfw/gif/{category}"
        data = await self.client.get(endpoint)
        return data.get("file", "")

    async def anal(self) -> str:
        return await self._get_nsfw_gif("anal")

    async def ass(self) -> str:
        return await self._get_nsfw_gif("ass")

    async def bdsm(self) -> str:
        return await self._get_nsfw_gif("bdsm")

    async def blowjob(self) -> str:
        return await self._get_nsfw_gif("blowjob")

    async def boobjob(self) -> str:
        return await self._get_nsfw_gif("boobjob")

    async def boobs(self) -> str:
        return await self._get_nsfw_gif("boobs")

    async def cum(self) -> str:
        return await self._get_nsfw_gif("cum")

    async def feet(self) -> str:
        return await self._get_nsfw_gif("feet")

    async def futa(self) -> str:
        return await self._get_nsfw_gif("futa")

    async def handjob(self) -> str:
        return await self._get_nsfw_gif("handjob")

    async def hentai(self) -> str:
        return await self._get_nsfw_gif("hentai")

    async def kitsune(self) -> str:
        return await self._get_nsfw_gif("kitsune")

    async def kuni(self) -> str:
        return await self._get_nsfw_gif("kuni")

    async def neko(self) -> str:
        return await self._get_nsfw_gif("neko")

    async def pussy(self) -> str:
        return await self._get_nsfw_gif("pussy")

    async def wank(self) -> str:
        return await self._get_nsfw_gif("wank")

    async def solo(self) -> str:
        return await self._get_nsfw_gif("solo")

    async def spank(self) -> str:
        return await self._get_nsfw_gif("spank")

    async def femdom(self) -> str:
        return await self._get_nsfw_gif("femdom")

    async def tentacle(self) -> str:
        return await self._get_nsfw_gif("tentacle")

    async def toys(self) -> str:
        return await self._get_nsfw_gif("toys")

    async def yuri(self) -> str:
        return await self._get_nsfw_gif("yuri")