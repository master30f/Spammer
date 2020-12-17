import discord

token = ""

client = discord.Client()
client.spamming = {}

@client.event
async def on_message(message):

    if message.content == 'start spam':
        client.spamming[message.channel] = True

    elif message.content == 'stop spam':
        client.spamming[message.channel] = False

    elif client.spamming[message.channel]:
        await message.channel.send(message.content)

client.run(token)
