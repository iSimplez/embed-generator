import discord
import os
import traceback
from dotenv import load_dotenv, find_dotenv
from colorama import Fore, Style
from discord.ext import commands
from controllers.deletecache import delete_pycache

load_dotenv(find_dotenv())
ID=os.getenv('APP_ID')

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=" ",
            intents=discord.Intents.all(), 
            application_id=ID,
            status=discord.Status.idle,
            activity=discord.Activity(type=discord.ActivityType.playing,name='Embed Generator 🪐'))

    async def setup_bot(self):
        await self.wait_until_ready()
        await self.tree.sync()
        print(f"{Fore.YELLOW} {Style.BRIGHT}🤖 {Style.RESET_ALL}", f"{Fore.YELLOW}| {Fore.YELLOW}{self.user} {Fore.YELLOW}{Fore.WHITE}[ {self.user.id} ]{Style.RESET_ALL}")

    async def setup_hook(self):
        # carregar extensões da pasta cogs
        print(f"{Fore.GREEN} {Style.BRIGHT}💻 {Style.RESET_ALL}", f"{Fore.GREEN}| Carregando comandos...{Style.RESET_ALL}")

        if os.path.isdir(f'./src/cogs'):
            for path in os.listdir(f'./src/cogs'):
                if path == "__pycache__":
                    continue

            for filename in os.listdir(f"./src/cogs/{path}"):
                    
                    if filename.endswith('.py'):
                        try:
                            await self.load_extension(f'src.cogs.{path}.{filename[:-3]}')
                            print(f"{Fore.CYAN} {Style.BRIGHT}✅ {Style.RESET_ALL}", f"{Fore.CYAN}| {filename}{Style.RESET_ALL}")
                            
                        except Exception:
                            print(f"{Fore.RED} {Style.BRIGHT}❌ {Style.RESET_ALL}", f"{Fore.RED}| Error loading.{Style.RESET_ALL} {Fore.YELLOW}{filename} {Style.RESET_ALL}")
                            
                            print(f'{Fore.LIGHTYELLOW_EX}')
                            traceback.print_exc()
                            print(f'{Style.RESET_ALL}')
            delete_pycache('.')
        self.loop.create_task(self.setup_bot())