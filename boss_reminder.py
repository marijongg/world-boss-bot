import os
from dotenv import load_dotenv
import discord
from discord.ext import tasks
from datetime import datetime

# ================== ENV ==================
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# ================== BOT SETUP ==================
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# ================== MESSAGE 1 (MAIN BOSS) ==================
BOSS_MESSAGE = (
    "[⚔️Boss] Get Ready! World Boss Spawn Starts at 7PM. See the in-game announcement or Boss Icon!\n\n"
    "Vale and Crossroad Ragnarok\n"
    "Field Boss Vargreif on Temple of Chaos 3F (Normal)\n"
    "Field Boss ‘Flame of Wraith Nargrim’ on Canyon 4F"
)

# Wednesday=2, Saturday=5
BOSS_DAYS = {2, 5}
BOSS_TIME = (18, 30)  # 6:30 PM

# ================== MESSAGE 2 (LOKI WARNING) ==================
LOKI_MESSAGE = "[⚔️Boss] Get Ready! Loki will spawn in 10 minutes!"

# Tuesday=1, Thursday=3, Saturday=5
LOKI_DAYS = {1, 3, 5}
LOKI_TIMES = {(11, 50), (21, 50)}  # 11:50 AM, 9:50 PM

# ================== EVENTS ==================
@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    boss_scheduler.start()
    loki_scheduler.start()

# ================== SCHEDULERS ==================
@tasks.loop(minutes=1)
async def boss_scheduler():
    now = datetime.now()
    if now.weekday() in BOSS_DAYS and (now.hour, now.minute) == BOSS_TIME:
        channel = await client.fetch_channel(CHANNEL_ID)
        await channel.send(BOSS_MESSAGE)
        print("📢 Boss reminder sent")

@tasks.loop(minutes=1)
async def loki_scheduler():
    now = datetime.now()
    if now.weekday() in LOKI_DAYS and (now.hour, now.minute) in LOKI_TIMES:
        channel = await client.fetch_channel(CHANNEL_ID)
        await channel.send(LOKI_MESSAGE)
        print("🔥 Loki reminder sent")

# ================== RUN ==================
client.run(TOKEN)
