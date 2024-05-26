import discord
from typing import Optional
from src.middleware.select.EmbedSelect import SelectOptions
from src.middleware.buttons.PainelButtons import SendButtonEmbed, DeleteButtonEmbed

class PainelViewer(discord.ui.View):
    def __init__(self, bot, embed, user, message:Optional[any]=None, edit:Optional[bool]=False):
        super().__init__(timeout=None)
        self.add_item(SelectOptions(bot, embed, user))
        self.add_item(SendButtonEmbed(bot, embed, user, message, edit))
        self.add_item(DeleteButtonEmbed(bot, embed, user))