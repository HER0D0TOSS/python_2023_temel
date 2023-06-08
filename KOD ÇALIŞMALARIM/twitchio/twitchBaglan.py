import twitchio.ext.commands.errors as err
from twitchio.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')
prefix = os.getenv('PREFIX')
channel = os.getenv('CHANNEL')

class roboTech(commands.Bot):
    
    def __init__(self):

        super().__init__(token=token, prefix=prefix, initial_channels=[channel] )
        
    async def event_ready(self):

        print(f'{self.nick} Hazır')
        print(f'{self.user_id} kullanici id')

    
    @commands.command()
    async def merhaba(self, ctx: commands.Context):
        kullaniciId = ctx.message.author.name
        mesajSaati = ctx.message.timestamp
        resimLinki = ctx.message.content

        print(f'{kullaniciId} kişisinin gönderdiği link{resimLinki}, gönderilen saat {mesajSaati} ')

        await ctx.send("wakdads")
    
        
        
bot = roboTech()
bot.run()