import os
from dotenv import load_dotenv, find_dotenv
from src import MyBot

load_dotenv(find_dotenv())
TOKEN=os.getenv('APP_TOKEN')    

bot = MyBot()
bot.remove_command("help")
bot.run(TOKEN)