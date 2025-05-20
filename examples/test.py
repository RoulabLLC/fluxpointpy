import asyncio
from fluxpointpy.client import FluxpointClient
from fluxpointpy.animal import animal
from fluxpointpy.color import color
from fluxpointpy.convert import convert
from fluxpointpy.imagegen import imagegen
from fluxpointpy.list import list
from fluxpointpy.meme import meme
from fluxpointpy.minecraft import minecraft
from fluxpointpy.misc import misc
from fluxpointpy.nsfwimages import nsfwimages
from fluxpointpy.nsfwgifs import nsfwgifs
from fluxpointpy.sfwgif import sfw_gif
from fluxpointpy.sfwimage import sfw_image
from fluxpointpy.utility import utility

async def main():

    async with FluxpointClient("FP-AYgGgk28ANVJJztICGOH5DuFWBSoy") as client:
        animal_api = animal(client)
        imagegen_api = imagegen(client)
        color_api = color(client)
        convert_api = convert(client)
        list_api = list(client)
        meme_api = meme(client)
        minecraft_api = minecraft(client)
        misc_api = misc(client)
        nsfwimages_api = nsfwimages(client)
        nsfwgifs_api = nsfwgifs(client)
        sfw_gif_api = sfw_gif(client)
        sfw_image_api = sfw_image(client)
        utility_api = utility(client)

        print("Animal Endpoints:")
        for fn in [
            animal_api.cat, animal_api.dog, animal_api.duck, animal_api.lizard,]:
            print(f"{fn.__name__.capitalize()}: {await fn()}")


        print("\nColor Endpoints:")
        print("Random Color:", await color_api.get_random_color())
        print("Color Info for 'blue':", await color_api.get_color_info("blue"))


        print("\nConvert Endpoints:")
        print("HTML to Markdown:", await convert_api.html_to_markdown("<strong>hi</strong>"))
        print("Markdown to HTML:", await convert_api.markdown_to_html("**hi**"))



        print("\nImageGen Custom:")
        payload = {
            "Base": {
                "type": "bitmap",
                "width": 2000,
                "height": 2000,
                "color": "#7289da"
            },
            "Images": [
                {
                    "type": "url",
                    "url": "https://img.fluxpoint.dev/thm/1422436083957760.jpg",
                    "width": 1000,
                    "height": 1000
                },
                {
                    "type": "bitmap",
                    "round": 160,
                    "x": 20,
                    "y": 240,
                    "width": 1220,
                    "height": 360,
                    "color": "0,0,0,80"
                }
            ],
            "Texts": [
                {
                    "text": "Hello",
                    "size": 120,
                    "x": 600,
                    "y": 1060
                }
            ]
        }
        print("Generate Custom Complex Image:", await imagegen_api.generate(payload))

        welcomepayload = {
            "username": "Builderb#0001",
            "avatar": "https://cdn.discordapp.com/avatars/190590364871032834/cbcf74d79018b6cb69546fd68c8d818a.png?size=320",
            "background": "#aaaaaa",
            "members": "member #1",
            "icon": "neko",
            "banner": "space",
            "color_welcome": "red",
            "color_username": "40,0,80",
            "color_members": "#ffffff"
        }
        print("Generate Welcome Image:", await imagegen_api.welcome(welcomepayload))

        print("\nList Templates:")
        print("Templates:", await list_api.templates())
        print("Banners:", await list_api.banners())
        print("Icons:", await list_api.icons())
        print("Fonts:", await list_api.fonts())

        print("\nMeme Endpoint:")
        print("Meme Image:", await meme_api.get_image("meme"))

        
        print("\nMinecraft Endpoints:")
        print("Ping:", await minecraft_api.ping_server("mc.hypixel.net"))
        print("UUID:", await minecraft_api.get_uuid("Notch"))
        print("Skin:", await minecraft_api.get_skin("Notch"))

        print("\nMisc:")
        print("Dad Joke:", await misc_api.get_dad_joke())
        print("User Info:", await misc_api.get_user_info())

        print("\nNSFW Images:")
        for fn in [nsfwimages_api.neko, nsfwimages_api.yuri, nsfwimages_api.anal]:
            print(f"{fn.__name__.capitalize()}: {await fn()}")

        print("\nNSFW GIFs:")
        for fn in [nsfwgifs_api.hentai, nsfwgifs_api.boobs, nsfwgifs_api.cum]:
            print(f"{fn.__name__.capitalize()}: {await fn()}")

        print("\nSFW Images:")
        for img_type in ["cat", "dog", "duck"]:
            print(f"{img_type.capitalize()}:", await sfw_image_api.get_image(img_type))

        print("\nSFW GIFs:")
        for gif_type in ["wink", "dance", "slap"]:
            print(f"{gif_type.capitalize()}:", await sfw_gif_api.get_gif(gif_type))

        print("\nUtility:")
        print("Unix to Date:", await utility_api.unix_to_date(1700000000, "%Y-%m-%d"))
        print("Snowflake to Date:", await utility_api.snowflake_to_date(22706878647631872, "%Y-%m-%d"))

if __name__ == "__main__":
    asyncio.run(main())