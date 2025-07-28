import aiohttp as ht
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

_API = os.getenv("URL")

async def aget(symb: str) -> float | int | str:
    try:
        async with ht.ClientSession() as req:
            async with req.get(f"{_API}ticker/price?symbol={symb}") as res:
                data = await res.json()
                return (data['price']).rstrip("0").rstrip(".")
    except KeyError:
        return -1
