from botLogic import *
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

eFunc = ' '

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$coinflip'):
        await message.channel.send("Coin Landed on:")
        await message.channel.send(coinflip())
    elif message.content.startswith('$time'):
        await message.channel.send("the date and time is:")
        await message.channel.send(cdate()) 
    elif message.content.startswith("$randnumb"):
        await message.channel.send(randnumb())
    elif message.content.startswith("$motivate"):
        await message.channel.send(mMessage())

client.run("No")

