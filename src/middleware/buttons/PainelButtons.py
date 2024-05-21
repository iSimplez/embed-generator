import discord
from asyncio import sleep
from src.middleware.select.EmbedSelect import SelectChannel

class SendButtonEmbed(discord.ui.Button):
    """
    Classe do Botão de Enviar

    ## Parâmetros:
    - bot: Recebe o valor de `MyBot()`
    - embed: Recebe o valor de `self.embed`, permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`.
    - user: Recebe o valor do usuário que está editando o embed. Ela serve para que outro usuário não possa interferir na criação do Embed
    """
    def __init__(self,bot, embed, user):
        self.bot=bot
        self.embed=embed
        self.user = user
        super().__init__(style=discord.ButtonStyle.green, label='Enviar Embed', emoji='<:verifycheck:1221520019582615624>', custom_id='sendembed')

    async def callback(self, interaction: discord.Interaction):
        if interaction.user == self.user:
            embed = discord.Embed(description=f'**Selecione o chat onde o Embed será enviado**', color=0x7700ff)
            embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
            await interaction.response.send_message(embed=embed,view=SelectChannel(self.bot, self.embed, self.user))
        else:
            embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse botão.**',color=0x7700ff)
            embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
            await interaction.response.send_message(embed=embed,ephemeral=True)

class DeleteButtonEmbed(discord.ui.Button):
    """
    Classe do Botão de Deletar

    ## Parâmetros:
    - bot: Recebe o valor de `MyBot()`
    - embed: Recebe o valor de `self.embed`, permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`.
    - user: Recebe o valor do usuário que está editando o embed. Ela serve para que outro usuário não possa interferir na criação do Embed
    """
    def __init__(self,bot,embed, user):
        self.bot = bot
        self.embed = embed
        self.user = user
        super().__init__(style=discord.ButtonStyle.red, label='Deletar Embed', custom_id='cancelembed',emoji='<:verifyuncheck:1147369405664202835>')

    async def callback(self, interaction: discord.Interaction):
        if interaction.user == self.user:
            await sleep(1)
            await interaction.message.delete()
        else:
            embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse botão.**',color=0x7700ff)
            embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
            await interaction.response.send_message(embed=embed,ephemeral=True)