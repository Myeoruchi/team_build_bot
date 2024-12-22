import os
import discord
from discord.ext import commands
from aiohttp import ClientSession
from dotenv import load_dotenv

class Bot(commands.AutoShardedBot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True  # DM을 보내기 위해서 필요
        super().__init__(
            command_prefix="!",
            intents=intents
        )
        self.session = None

    async def setup_hook(self):
        self.session = ClientSession()
        await self.load_extension("default")

        self.tree.copy_global_to(guild=discord.Object(id=os.getenv('TEST_GUILD_ID')))
        await self.tree.sync()
    
    async def on_ready(self):
        print("Bot is ready")
        activity = discord.Game("/명령어")
        await self.change_presence(status=discord.Status.online, activity=activity)

    async def close(self):
        await super().close()
        if self.session:
            await self.session.close()
            
if __name__=="__main__":
    load_dotenv()
    bot = Bot()
    bot.run(os.getenv('TOKEN'))