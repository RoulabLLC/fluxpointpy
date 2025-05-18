from .client import FluxpointClient

class nsfwimages:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def _get_nsfw_image(self, category: str) -> str:
        endpoint = f"/nsfw/img/{category}"
        data = await self.client.get(endpoint)
        return data.get("file", "")

    async def anal(self) -> str:
        return await self._get_nsfw_image("anal")

    async def anus(self) -> str:
        return await self._get_nsfw_image("anus")

    async def ass(self) -> str:
        return await self._get_nsfw_image("ass")

    async def azurlane(self) -> str:
        return await self._get_nsfw_image("azurlane")

    async def bdsm(self) -> str:
        return await self._get_nsfw_image("bdsm")

    async def blowjob(self) -> str:
        return await self._get_nsfw_image("blowjob")

    async def boobs(self) -> str:
        return await self._get_nsfw_image("boobs")

    async def cosplay(self) -> str:
        return await self._get_nsfw_image("cosplay")

    async def cum(self) -> str:
        return await self._get_nsfw_image("cum")

    async def feet(self) -> str:
        return await self._get_nsfw_image("feet")

    async def femdom(self) -> str:
        return await self._get_nsfw_image("femdom")

    async def futa(self) -> str:
        return await self._get_nsfw_image("futa")

    async def gasm(self) -> str:
        return await self._get_nsfw_image("gasm")

    async def holo(self) -> str:
        return await self._get_nsfw_image("holo")

    async def kitsune(self) -> str:
        return await self._get_nsfw_image("kitsune")

    async def lewd(self) -> str:
        return await self._get_nsfw_image("lewd")

    async def neko(self) -> str:
        return await self._get_nsfw_image("neko")

    async def nekopara(self) -> str:
        return await self._get_nsfw_image("nekopara")

    async def pantsu(self) -> str:
        return await self._get_nsfw_image("pantsu")

    async def pantyhose(self) -> str:
        return await self._get_nsfw_image("pantyhose")

    async def peeing(self) -> str:
        return await self._get_nsfw_image("peeing")

    async def petplay(self) -> str:
        return await self._get_nsfw_image("petplay")

    async def pussy(self) -> str:
        return await self._get_nsfw_image("pussy")

    async def slimes(self) -> str:
        return await self._get_nsfw_image("slimes")

    async def solo(self) -> str:
        return await self._get_nsfw_image("solo")

    async def swimsuit(self) -> str:
        return await self._get_nsfw_image("swimsuit")

    async def tentacle(self) -> str:
        return await self._get_nsfw_image("tentacle")

    async def thighs(self) -> str:
        return await self._get_nsfw_image("thighs")

    async def trap(self) -> str:
        return await self._get_nsfw_image("trap")

    async def yaoi(self) -> str:
        return await self._get_nsfw_image("yaoi")

    async def yuri(self) -> str:
        return await self._get_nsfw_image("yuri")
