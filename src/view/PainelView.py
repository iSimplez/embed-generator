import discord
from src.middleware.select.EmbedSelect import SelectOptions
from src.middleware.buttons.PainelButtons import SendButtonEmbed, DeleteButtonEmbed

class PainelViewer(discord.ui.View):
    def __init__(self,bot,embed,user):
        super().__init__(timeout=None)
        self.add_item(SelectOptions(bot, embed, user))
        self.add_item(SendButtonEmbed(bot, embed, user))
        self.add_item(DeleteButtonEmbed(bot, embed, user))