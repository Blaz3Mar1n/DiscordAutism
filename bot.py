import discord
import requests
from discord.ext import commands
def pewds():
    r = requests.get("https://bastet.socialblade.com/youtube/lookup?query=" + "UC-lHJZR3Gqxm24_Vd_AJ5Yw")
    r = r.content
    if r[0] == 'b' :
        r = r[1:]
    return int(r)
def tseries():
    r = requests.get("https://bastet.socialblade.com/youtube/lookup?query=" + "UCq-Fj5jknLsUf-MWSy4_brA")
    r = r.content
    if r[0] == 'b' :
        r = r[1:]
    return int(r)
client = commands.Bot(command_prefix = '*')
def getresponse(talk) :
    r = requests.get("https://some-random-api.ml/chatbot/?message="+talk)
    r = r.content
    print(r)
    if r[0] == 'b' :
        r = r[1:]
    resp = str(r)
    print(resp)
    resp = resp[15:-3]
    return(resp)
@client.event
async def on_ready() :
    print('Bot is ready')

@client.event
async def on_message(message) :
    sent = message.content
    id = client.get_guild(565603722529603585)
    if message.content.find('*pewds') != -1 :
        print('Pewds : '+str(pewds())+'      T-series : '+str(tseries())+'       Subgap : '+str(int(str(pewds()))-int(str(tseries()))))
        await message.channel.send('Pewds : '+str(pewds())+'      T-series : '+str(tseries())+'       Subgap : '+str(int(str(pewds()))-int(str(tseries()))))
    if message.content.find('*talk') != -1 :
        talk = ''
        print(sent)
        start = False
        for i in sent :
            if i == 'k' and start == False :
                start = True
            elif start == True :
                talk+=i
        talk = talk[1:]
        print(talk)
        if talk == 'Are you subscribed to PewDiePie?' :
             await message.channel.send('Yes.I learned my lesson.')
        else :
            rep = getresponse(talk)
            print(rep)
            await message.channel.send(rep)
    if message.content.find('*help') != -1:
        await message.channel.send(''' ```Commands :
        
        pewds- displays pewdiepie and tseries subcount + subgap
        
        talk- you can talk to the bot.
              note: this is still BETA which means
              he is highly autistic.
              While talking you have to be carefull about writing and watch
              out about question marks.
              
              EXAMPLE: talk Hello!
        
        MORE COMING SOON    ``` ''')
client.run('NTcxNzY1ODcxNTEzNDM2MTYx.XMShnQ.l3ZyZBjgK9qEHzdDxJ8U-a8qW80')
client.run(str(os.environ.get('BOT_TOKEN')))
