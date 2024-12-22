import discord
from discord import app_commands
from discord.ext import commands

class Default(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="핑")
    async def ping(self, interaction: discord.Interaction) -> None:
        """봇의 응답속도를 알려줍니다."""
        
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"퐁! `{latency}ms`")

    @app_commands.command(name="도움말")
    async def help(self, interaction: discord.Interaction) -> None:
        """봇의 정보를 알려줍니다."""
        
        embed = discord.Embed(
            colour=0x7FFFD4,
            description="""
- 발로란트 내전용으로 제작된 디스코드 봇입니다.
- 점수를 기반으로 하는 팀 밸런싱, 맵 추첨 등의 기능을 제공합니다.
- 명령어 목록을 보시려면 `/명령어`나 하단 버튼을 클릭해주세요.\n
[봇 초대하기](https://discord.com/oauth2/authorize?client_id=1181618445368954881)
            """   
        )
        embed.set_author(
            name=f"{self.bot.user.name} 소개",
            icon_url=f"{self.bot.user.avatar}"
        )
        
        # 명령어 보기 버튼 생성
        view = discord.ui.View()

        button = discord.ui.Button(
            label="명령어 목록 보기",
            style=discord.ButtonStyle.primary,
            custom_id="show_command_list",
        )
        button.callback = self.button_callback
        view.add_item(button)

        await interaction.response.send_message(embed=embed, view=view)

    @app_commands.command(name="명령어")
    async def list(self, interaction: discord.Interaction) -> None:
        """봇의 명령어 목록을 보여줍니다."""
        await self.show_command_list(interaction)

    async def button_callback(self, interaction: discord.Interaction) -> None:
        if interaction.data['custom_id'] == "show_command_list":
            await self.show_command_list(interaction)
    
    async def show_command_list(self, interaction: discord.Interaction) -> None:
        """봇의 명령어 목록을 보여주는 내부 메서드."""
        
        embed = discord.Embed(
            color=0x7FFFD4,
            title=f"{self.bot.user.name} 명령어 목록"
        )
        embed.add_field(name="/핑", value="봇의 응답속도를 알려줍니다.", inline=False)
        embed.add_field(name="/도움말", value="봇의 정보를 알려줍니다.", inline=False)
        embed.add_field(name="/명령어", value="봇의 명령어 목록을 보여줍니다.", inline=False)
        
        await interaction.response.send_message(embed=embed)
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Default(bot))