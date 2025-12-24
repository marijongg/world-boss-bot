import os
import discord
from discord.ext import tasks
from datetime import datetime

# ================= CONFIG =================

TOKEN = os.getenv("DISCORD_TOKEN")  # Set in environment variable
CHANNEL_ID = 1452670267267485857     # <-- PUT YOUR CHANNEL ID HERE

MESSAGE = (
    "[⚔️Boss] Get Ready! Starts at 7PM. See the in-game announcement or Boss Icon!\n\n"
    "Vale and Crossroad Ragnarok\n"
    "Field Boss Vargreif on Temple of Chaos 3F (Normal)\n"
    "Field Boss ‘Flame of Wraith Nargrim’ on Canyon 4F"
)

# Wednesday = 2, Saturday = 5
ALLOWED_DAYS = {2, 5}

# 6:30 PM
ALLOWED_TIME = (18, 30)

# ==========================================

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    scheduler.start()

@tasks.loop(minutes=1)
async def scheduler():
    now = datetime.now()
    if now.weekday() in ALLOWED_DAYS and (now.hour, now.minute) == ALLOWED_TIME:
        channel = await client.fetch_channel(CHANNEL_ID)
        await channel.send(MESSAGE)
        print("📢 Boss reminder sent")

client.run(TOKEN)
