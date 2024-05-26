import discord
from discord.ext import commands
from discord import app_commands
from src.view.PainelView import PainelViewer
from typing import Union, Optional

class EmbedCommands(commands.Cog): # Cria a Classe onde ela exige que o parametro `bot` seja fornecido na sua chamada.
    def __init__(self,bot) -> None:
        self.bot=bot
        super().__init__()

    embed = app_commands.Group(name='embed', description='Embeds commands') # Cria o grupo de comandos relacionado a Embeds.

    @embed.command(name='create', description='｢Discord｣ Abre um painel onde você poderá editar o seu Embed.') # Comando que cria o Embed, abre um painel onde criaremos o Embed.
    async def create(self,interaction:discord.Interaction):
        embed = discord.Embed(title='Esse é o **Título** do Embed.',description='Essa é a **Descrição** do Embed', color=0x7700ff)
        embed.set_author(name='Esse é o Author do Embed',icon_url=self.bot.user.avatar)
        embed.set_image(url=(await self.bot.fetch_user(self.bot.user.id)).banner)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text='Esse é o rodapé do Embed',icon_url=self.bot.user.avatar)
        await interaction.response.send_message(embed=embed,view=PainelViewer(self.bot,embed,interaction.user)) # Envia o painel no Chat que ocorreu a interação.

    @embed.command(name='edit', description='｢Discord｣ Abre um painel onde você poderá editar um Embed já existente.') # Comando que edita um Embed já existente, abre um painel com informações do embed específicado. ***OBS: O bot só poderá editar os embeds que foram enviados por ele, o mesmo serve para WebHooks.***
    @app_commands.describe(id='Forneça o id da mensagem que você deseja editar.', channel='Forneça o Chat onde está localizada a mensagem.')
    async def edit(self, interaction:discord.Interaction, channel:Optional[Union[discord.TextChannel, discord.Thread]], id:str):
                if channel == None:
                     channel = interaction.channel
                if (message := await channel.fetch_message(int(id))).author.id == self.bot.user.id:
                    if message.embeds:
                        embed = message.embeds[0]
                        await interaction.response.send_message(embed=embed,view=PainelViewer(bot=self.bot, embed=embed, user=interaction.user, message=message, edit=True))

    @embed.command(name='clone', description='｢Discord｣ Abre um painel onde você poderá editar o Embed que você clonou.') # Comando que clona um Embed já existente, abre um painel com as informações do Embed específicado.
    @app_commands.describe(link="Link do embed que você deseja clonar.")
    async def clone(self, interaction:discord.Interaction, link:str):
        await interaction.response.send_message("**<:verifycheck:1221520019582615624> | Estamos trabalhando continuamente na criação dessa função. Ela estará disponível em uma atualização futura.**",ephemeral=True) # Envia o painel no Chat que ocorreu a interação.

async def setup(bot):
    await bot.add_cog(EmbedCommands(bot))