from twitchio.ext import commands
from dotenv import load_dotenv
import os

veriler = []

load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        
        super().__init__(token='fegic0vb31ac1g6403nb12daupp7ol', prefix='!', initial_channels=['roboteech'])

    async def event_ready(self):
        
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        userId = ctx.message.author.name
        messageHour = ctx.message.timestamp
        pictureLink = ctx.message.content

        birlestir ={"id": userId, "saat:": messageHour,"resim" : pictureLink }
        
        liste_durum = (len(veriler))

        if liste_durum == 0 :
            print("çizin başlıyor")
            #fonksiyonu çalıştırır  
        else:
            print("dolu")
            # sıra saymaya başla   

        veriler.append(birlestir)
        
        

        print(veriler)
        

        await ctx.send(f'çizim başlıyor {veriler[0]["id"]}, çizim süresi 3 dakika')
    
    
            


            


bot = Bot()
bot.run()