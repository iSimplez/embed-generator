import discord
from src.middleware.buttons.WebhookButtons import YesWebhookButton, NoWebhookButton

class WebhookViewer(discord.ui.View):
    def __init__(self,embed, bot, channel,user):
        super().__init__(timeout=None)
        self.add_item(YesWebhookButton(bot, embed, channel, user))
        self.add_item(NoWebhookButton(bot, embed ,channel, user))