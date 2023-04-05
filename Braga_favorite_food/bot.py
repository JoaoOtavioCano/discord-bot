import discordToken
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#emoji = discord.Emoji('💩')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/braga'):
        await message.channel.send('💩 __**MERDA**__ 💩')

client.run(discordToken.token())