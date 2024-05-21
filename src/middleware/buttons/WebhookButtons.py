import discord
from asyncio import sleep
from src.middleware.modal.EmbedModal import BotAssets

class YesWebhookButton(discord.ui.Button):
    """
    Classe do Botão de Webhook, caso o usuário queira enviar a mensagem como um `Webhook`.

    ## Parâmetros:
    - bot: `discord.Client`.
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`.
    - channel: Recebe o objeto do `channel` em que a mensagem será enviada. 
    - user: Recebe o objeto do `user` que está editando o embed. Ela serve para que outro usuário não possa interferir na criação do Embed.
    """
    def __init__(self,bot, embed, channel,user):
        self.bot = bot
        self.embed = embed
        self.channel = channel
        self.user = user
        super().__init__(style=discord.ButtonStyle.green, label='Sim', custom_id='yesbutton',emoji='<:verifycheck:1221520019582615624>')

    async def callback(self, interaction: discord.Interaction):
        if interaction.user == self.user:
            await interaction.response.send_modal(BotAssets(self.bot, self.embed, self.channel))
            await sleep(1)
            await interaction.message.delete()
        else:
            embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse botão.**',color=0x7700ff)
            embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
            await interaction.response.send_message(embed=embed,ephemeral=True)

class NoWebhookButton(discord.ui.Button):
    """
    Classe do Botão de Webhook, caso o usuário `não` queira enviar a mensagem como um `Webhook`.

    ## Parâmetros:
    - bot: `discord.Client`.
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`.
    - channel: Recebe o objeto do `channel` em que a mensagem será enviada. 
    - user: Recebe o objeto do `user` que está editando o embed. Ela serve para que outro usuário não possa interferir na criação do Embed.
    """
    def __init__(self,bot, embed, channel, user):
        self.bot = bot
        self.channel= channel
        self.embed = embed
        self.user = user
        super().__init__(style=discord.ButtonStyle.red, label='Não', custom_id='nobutton',emoji='<:verifyuncheck:1147369405664202835>')
    
    async def callback(self, interaction: discord.Interaction):
            if interaction.user == self.user: 
                await self.channel.send(embed=self.embed)
                embed = discord.Embed(description=f'**<:verifycheck:1221520019582615624> | Embed enviado com sucesso em {self.channel.mention}**', color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,delete_after=5)
                await sleep(1)
                await interaction.message.delete()
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse botão.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)