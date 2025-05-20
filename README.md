# Fluxpoint Python API Client

Unofficial Python async wrapper for the [Fluxpoint API](https://fluxpoint.dev). Includes support for all major endpoints such as image generation, conversion, NSFW, color utilities, Minecraft, memes, and more.

## Features

* Async support via `aiohttp`
* Organized into endpoint classes
* Full support for:

  * SFW/NSFW images & gifs
  * Meme/image generators
  * Welcome/custom image builders
  * Minecraft utilities
  * Color & utility tools
  * HTML/Markdown conversion

## Installation

```bash
pip install aiohttp
```

## Getting Started

```python
from fluxpointpy.client import FluxpointClient
from animal import animal

async with FluxpointClient("YOUR_API_TOKEN") as client:
    api = animal(client)
    print(await api.cat())
```

## Modules

### `client.py`

Handles aiohttp session and request helpers.

### `animal.py`

Real animal image endpoints (e.g. cat, dog, panda, etc).

### `color.py`

* `get_random_color()`
* `get_color_info(name)`

### `convert.py`

* `html_to_markdown(html)`
* `markdown_to_html(md)`
* `convert_image(bytes, to_format)`

### `imagegen.py`

* `generate_template(template, params)`
* `generate_custom_image(data)`
* `test_error_response()`

### `imagegen_custom.py`

* `generate(payload: dict)`
* `welcome(payload: dict)`

### `list.py`

Fetches available templates, fonts, banners, icons.

### `meme.py`

Get random meme images.

### `minecraft.py`

* `ping_server(host, port)`
* `get_uuid(player)`
* `get_skin(player)`

### `misc.py`

* `get_dad_joke()`
* `get_user_info()`

### `nsfwimages.py`

All `/nsfw/img/{type}` endpoints (e.g. anal, neko, cum...)

### `nsfwgifs.py`

All `/nsfw/gif/{type}` endpoints (e.g. hentai, spank...)

### `sfw_image.py` / `sfw_gif.py`

General-purpose sfw image/gif retrieval.

### `utility.py`

* `unix_to_date(unix, format)`
* `snowflake_to_date(snowflake, format)`

## Testing

Run the full test suite:

```bash
python test.py
```

## License

MIT

## Contact

For questions/issues join: [Fluxpoint Discord](https://discord.gg/fluxpoint) or contact repo author.

---

> This project is not officially affiliated with Fluxpoint.
