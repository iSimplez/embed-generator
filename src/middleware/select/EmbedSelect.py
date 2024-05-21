import discord
from asyncio import sleep
from src.middleware.modal.EmbedModal import *
from src.view.WebhookView import WebhookViewer

class SelectChannel(discord.ui.View):
    """
    Class SelectChannel, onde o usuário poderá escolher o `chat` onde a mensagem será enviada.

    ## Parâmetros:
    - bot: `discord.Client`.
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`.
    - user: Recebe o objeto do `user` que está editando o embed. Ela serve para que outro usuário não possa interferir na criação do Embed.
    """
    def __init__(self,bot, embed,user):
        self.bot = bot
        self.embed = embed
        self.user = user
        super().__init__(timeout=7200)
    
    @discord.ui.select(cls=discord.ui.ChannelSelect, channel_types=[discord.ChannelType.text],placeholder='Selecione um chat...')
    async def select_channels(self, interaction: discord.Interaction, select: discord.ui.ChannelSelect):
            if interaction.user == self.user:
                channel = self.bot.get_channel(select.values[0].id)
                embed = discord.Embed(description=f'**Você deseja alterar o Nome e Icon do bot na mensagem que será enviada?**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed, view=WebhookViewer(self.embed,self.bot,channel,self.user))
                await sleep(1)
                await interaction.message.delete()
            
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)
                
class SelectOptions(discord.ui.Select):
    """
    Class SelectOptions, onde o usuário poderá escolher as `opções` para editar o embed.

    ## Parâmetros:
    - bot: `discord.Client`.
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`.
    - user: Recebe o objeto do `user` que está editando o embed. Ela serve para que outro usuário não possa interferir na criação do Embed.
    """
    def __init__(self,bot, embed,user):
        self.bot = bot
        self.embed = embed
        self.user = user
        
        options = [
            discord.SelectOption(label='Edite o Autor.', description='Edite quem será o autor da mensagem.',value='Author'),
            discord.SelectOption(label='Edite a Messagem.', description='Edite o Título e a mensagem do embed.',value='Message'),
            discord.SelectOption(label='Edite a Thumbnail.', description='Edite qual será a Thumbnail do embed.', value='Thumbnail'),
            discord.SelectOption(label='Edite a Imagem.', description='Edite qual será a Imagem do embed.', value='Image'),
            discord.SelectOption(label='Edite o Rodapé.', description='Edite qual será o rodapé do embed.', value='Footer'),
            discord.SelectOption(label='Edite a Cor.', description='Edite qual será a cor do embed.', value='Color'),
            discord.SelectOption(label='Add Field.',description='Adicione um campo.', value='Add'),
            discord.SelectOption(label='Remove Field.',description='Remova um campo.' ,value='Remove'),
        ]
        super().__init__(placeholder='Edite o Embed', min_values=1,max_values=1, options=options,custom_id='SelectOptions:persistent')

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Author":
            if interaction.user == self.user:
                await interaction.response.send_modal(AuthorModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)
        
        elif self.values[0] == "Message":
            if interaction.user == self.user:
                await interaction.response.send_modal(MessageModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)

        elif self.values[0] == "Thumbnail":
            if interaction.user == self.user:
                await interaction.response.send_modal(ThumbModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)

        elif self.values[0] == "Image":
            if interaction.user == self.user:
                await interaction.response.send_modal(ImageModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)

        elif self.values[0] == "Footer":
            if interaction.user == self.user:
                await interaction.response.send_modal(FooterModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)

        elif self.values[0] == "Color":
            if interaction.user == self.user:
                await interaction.response.send_modal(ColorModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)

        elif self.values[0] == "Add":
            if interaction.user == self.user:
                await interaction.response.send_modal(AddModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)

        elif self.values[0] == "Remove":
            if interaction.user == self.user:
                await interaction.response.send_modal(RemoveModal(self.embed))
            else:
                embed = discord.Embed(description=f'**<:verifyuncheck:1147369405664202835> | Somente {self.user.mention} tem permissão para interagir com esse comando.**',color=0x7700ff)
                embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
                await interaction.response.send_message(embed=embed,ephemeral=True)
