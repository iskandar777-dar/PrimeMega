from PrimeMega.config import API_ID, API_HASH, BOT_TOKEN
import logging
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN,
    in_memory = True,
    plugins=dict(root="PrimeMega"),
)
