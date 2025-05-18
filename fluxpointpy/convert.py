from .client import FluxpointClient
import aiohttp

class convert:
    def __init__(self, client: FluxpointClient):
        self.client = client

    async def html_to_markdown(self, html: str) -> str:
        body = {"html": html}
        data = await self.client.post("/convert/html-markdown", json=body)
        return data.get("markdown", "")

    async def markdown_to_html(self, markdown: str) -> str:
        body = {"markdown": markdown}
        data = await self.client.post("/convert/markdown-html", json=body)
        return data.get("html", "")

    async def convert_image(self, image_data: bytes, to_format: str, quality: int = 100) -> bytes:
        endpoint = f"/convert/image-{to_format}"
        params = {"quality": quality}
        form = aiohttp.FormData()
        form.add_field("file", image_data, filename="upload", content_type="application/octet-stream")

        async with self.client.session.post(f"{self.client.BASE_URL}{endpoint}", params=params, data=form) as response:
            response.raise_for_status()
            return await response.read()
