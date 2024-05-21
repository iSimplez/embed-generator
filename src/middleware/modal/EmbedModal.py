import discord
import requests

class BotAssets(discord.ui.Modal):
    """
    Classe do Modal do Webhook, onde o usuário poderá editar as informações básicas do `Webhook`.

    ## Parâmetros:
    - bot: `discord.Client`.
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`.
    - channel: Recebe o objeto do `channel` em que a mensagem será enviada.

    ## Explicação:
    - self.botname: Nome do `Webhook`.
    - self.boticon: URL da imagem do `Webhook`.
    """
    def __init__(self, bot, embed, channel):
        self.bot = bot
        self.embed = embed
        self.channel = channel
        super().__init__(title='Edite o Nome e Icon do Bot')

        self.botname = discord.ui.TextInput(label='Nome', placeholder='Escreva aqui o Nome do Bot', default=self.bot.user.name, style=discord.TextStyle.short,max_length=32,required=False)        
        self.boticon = discord.ui.TextInput(label='Icon', placeholder='Escreva aqui a URL do Icon do Bot', default=self.bot.user.avatar.url,style=discord.TextStyle.short,required=False)
        self.add_item(self.botname)
        self.add_item(self.boticon)
                
    async def on_submit(self, interaction: discord.Interaction):
        webhook = await self.channel.create_webhook(name=self.botname, avatar=requests.get(self.boticon).content, reason='Webhook Embed')
        await webhook.send(embed=self.embed)
        embed = discord.Embed(description=f'**<:verifycheck:1221520019582615624> | Embed enviado com sucesso em {self.channel.mention}**', color=0x7700ff)
        embed.set_footer(text='Todos os direitos reservados por Simplez World 🌎 ©', icon_url=self.bot.user.avatar)
        await interaction.response.send_message(embed=embed,delete_after=5)
        
class AuthorModal(discord.ui.Modal):
    """
    Classe do Modal do Author, onde o usuário poderá editar as informações básicas do `Autor`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.name: Nome do `Autor`.
    - self.icon: URl da imagem do `Autor`.
    """
    def __init__(self,embed):
        self.embed=embed
        super().__init__(title='Edite o Autor do Embed', timeout=None, custom_id='author')

        self.name = discord.ui.TextInput(label='Nome do Autor',placeholder='Escreva aqui o nome do Autor...',default=embed.author.name,style=discord.TextStyle.short,max_length=50,required=False)
        self.icon = discord.ui.TextInput(label='Icon do Autor', placeholder='Escreva aqui o link a URL do icon do Autor...',default=embed.author.icon_url,style=discord.TextStyle.short,max_length=250,required=False)
        self.add_item(self.name)
        self.add_item(self.icon)
    async def on_submit(self, interaction: discord.Interaction):
        self.embed.set_author(name=self.name,icon_url=self.icon)
        await interaction.response.edit_message(embed=self.embed)

class MessageModal(discord.ui.Modal):
    """
    Classe do Modal da Mensagem, onde o usuário poderá editar as informações básicas da `Mensagem`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.Title: Título do `Embed`.
    - self.description: Mensagem do `Embed`. 
    """
    def __init__(self,embed):
        self.embed=embed
        super().__init__(title='Edite a mensagem do Embed', timeout=None, custom_id='Message')
        self.Title = discord.ui.TextInput(label='Título',placeholder='Escreva aqui o Título do Embed...',default=embed.title,style=discord.TextStyle.short,max_length=50,required=False)
        self.description = discord.ui.TextInput(label='Descrição',placeholder='Escreva aqui a Descrição do Embed...',default=embed.description,style=discord.TextStyle.long,required=False)
        self.add_item(self.Title)
        self.add_item(self.description)

    async def on_submit(self, interaction: discord.Interaction):
        self.embed.title = self.Title.value
        self.embed.description = self.description.value
        await interaction.response.edit_message(embed=self.embed)

class ThumbModal(discord.ui.Modal):
    """
    Classe do Modal do Thumbnail, onde o usuário poderá editar as informações básicas do `Thumbnail`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.thumb: URL da imagem do `Thumbnail`.
    """
    def __init__(self,embed):
        self.embed=embed
        super().__init__(title='Edite a Thumbnail do Embed', timeout=None, custom_id='Thumb')

        self.thumb = discord.ui.TextInput(label='Thumbnail',placeholder='Escreva aqui a URL do Thumbnail do Embed...',default=embed.thumbnail.url,style=discord.TextStyle.short,max_length=250,required=False)
        self.add_item(self.thumb)

    async def on_submit(self, interaction: discord.Interaction):
        self.embed.set_thumbnail(url=self.thumb)
        await interaction.response.edit_message(embed=self.embed)

class ImageModal(discord.ui.Modal):
    """
    Classe do Modal da Imagem, onde o usuário poderá editar as informações básicas da `Imagem`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.image: URL da `Imagem`.
    """
    def __init__(self,embed):
        self.embed=embed
        super().__init__(title='Edite a Imagem do Embed', timeout=None, custom_id='Image')
    
        self.image = discord.ui.TextInput(label='Imagem',placeholder='Escreva aqui a URL da Imagem do Embed...',default=embed.image.url,style=discord.TextStyle.short,max_length=250,required=False)
        self.add_item(self.image)

    async def on_submit(self, interaction: discord.Interaction):
        self.embed.set_image(url=self.image)
        await interaction.response.edit_message(embed=self.embed)

class FooterModal(discord.ui.Modal):
    """
    Classe do Modal do Footer, onde o usuário poderá editar as informações básicas do `Footer`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.text: Pequena mensagem do `Footer(rodapé)`.
    - self.icon: URL da imagem do icone do `Footer(rodapé)`.
    """
    def __init__(self,embed):
        self.embed=embed
        super().__init__(title='Edite o Rodapé do Embed',timeout=None,custom_id='Footer')

        self.text = discord.ui.TextInput(label='Texto do Rodapé',placeholder='Escreva aqui o Rodapé...',default=embed.footer.text,style=discord.TextStyle.short,max_length=50,required=False)
        self.icon = discord.ui.TextInput(label='Icon Url',placeholder='Escreva aqui a URL do Rodapé...',default=embed.footer.icon_url,style=discord.TextStyle.short,max_length=250,required=False)
        self.add_item(self.text)
        self.add_item(self.icon) 

    async def on_submit(self, interaction: discord.Interaction):
        self.embed.set_footer(text=self.text.value,icon_url=self.icon)
        await interaction.response.edit_message(embed=self.embed)

class ColorModal(discord.ui.Modal):
    """
    Classe do Modal da Cor, onde o usuário poderá editar as informações básicas da `Cor`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.color: Hex da cor do `Embed`.
    """
    def __init__(self, embed):
        self.embed=embed
        super().__init__(title='Color', timeout=None, custom_id='Color')

        self.color = discord.ui.TextInput(label='Edite a Cor do Embed',placeholder='Escreva aqui a cor no formato Hexadecimal...',default='0d1018',style=discord.TextStyle.short,required=False)
        self.add_item(self.color)

    async def on_submit(self, interaction:discord.Interaction):
        self.embed.color = discord.Color(int(self.color.value, 16))
        await interaction.response.edit_message(embed=self.embed)

class AddModal(discord.ui.Modal):
    """
    Classe do Modal AddField, onde o usuário poderá adicionar um `Field`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.fieldname: Nome do ``Campo`` que será adicionado.
    - self.fieldvalue: Mensagem do ``Campo`` que será adicionado.
    - self.fieldinline: ``Boolean``.
    """
    def __init__(self,embed):
        self.embed=embed
        super().__init__(title='Add Field', timeout=None, custom_id='addfield')

        self.fieldname = discord.ui.TextInput(label='Nome',placeholder='Escreva aqui o nome do Field...',style=discord.TextStyle.short,required=False)
        self.fieldvalue = discord.ui.TextInput(label='Value',placeholder='Escreva aqui a mensagem do Field...',style=discord.TextStyle.paragraph,required=False)
        self.fieldinline = discord.ui.TextInput(label='Inline',placeholder='Escreva aqui se será na mesma linha. True ou False...',default='True',style=discord.TextStyle.short,required=False)
        self.add_item(self.fieldname)
        self.add_item(self.fieldvalue)
        self.add_item(self.fieldinline)

    async def on_submit(self, interaction: discord.Interaction):
        self.embed.add_field(name=self.fieldname.value, value=self.fieldvalue.value,inline=bool(self.fieldinline.value))
        await interaction.response.edit_message(embed=self.embed)

class RemoveModal(discord.ui.Modal):
    """
    Classe do Modal do RemoveField, onde o usuário poderá remover um `Field`.

    ## Parâmetros:
    - embed: Objeto `discord.Embed` , permitindo acessar quaisquer um de seus atributos durante a instância da class `SelectOption`. 
    
    ## Explicação:
    - self.index: `Campo` que será deletado, `0` sempre será o `1°` campo e assim por diante.
    """
    def __init__(self,embed):
        self.embed=embed
        super().__init__(title='Remover Field', timeout=None, custom_id='removefield')

        self.index = discord.ui.TextInput(label='Index',placeholder='Escreva aqui a númeração do Field q será removido...',default='1',style=discord.TextStyle.short)
        self.add_item(self.index)

    async def on_submit(self, interaction: discord.Interaction):
        field = int(self.index.value) - 1
        self.embed.remove_field(index=field)
        await interaction.response.edit_message(embed=self.embed)