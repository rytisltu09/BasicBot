import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def main():
    for file in os.listdir("cogs"):
        if file.startswith("__") or not file.endswith(".py"):
            continue
        await bot.load_extension(f"cogs.{file[:-3]}")
    await bot.start(TOKEN)

@bot.event
async def on_ready():
    guild = discord.Object(id=1492817371998453760)
    await bot.tree.sync(guild=guild)
    print(f"{bot.user} has connected to Discord!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())