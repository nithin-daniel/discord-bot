# Import Discord Package
import discord
from discord.ext import commands

# Client (our bot)
# client = discord.Client() # Documentation
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='--',intents=intents)
@client.command(name='version')
async def version(context):
    general_channel = client.get_channel('') # Paste Channel id in get_channel('channel_id')
    myEmbed = discord.Embed(title="Current Version", description="The bot is in Version on 1.0 ",color=0x00ff00)
    myEmbed.add_field(name="Version Code:",value="v1.0.0",inline=False)
    myEmbed.add_field(name="Date Released", value="July 18th, 2020",inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Nithin Daniel")
    await context.message.channel.send(embed=myEmbed)
    # await general_channel.send(embed=myEmbed)

@client.event
async def on_ready():
    # DO STUFF.....
    general_channel = client.get_channel() # Paste Channel id in get_channel(channel_id)
    await general_channel.send('Hello World!')

@client.event
async def on_disconnect():
    general_channel = client.get_channel() # Paste Channel id in get_channel(channel_id)
    await general_channel.send('Good Bye')
@client.event
async def on_message(message):
    # print(type(message.content))
    if message.content == 'what is the version':
        general_channel = client.get_channel('') # Paste Channel id in get_channel('channel_id')
        myEmbed = discord.Embed(title="Current Version", description="The bot is in Version on 1.0 ",color=0x00ff00)
        myEmbed.add_field(name="Version Code:",value="v1.0.0",inline=False)
        myEmbed.add_field(name="Date Released", value="July 18th, 2020",inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="Nithin Daniel")
        await general_channel.send(embed=myEmbed)
    await client.process_commands(message)


# Run the client on the server
client.run('') # Paste Bot Token into the run('TOKEN')




# Resource Used
# https://www.youtube.com/playlist?list=PLfpeXtDSa8rWW02LOjl2IW9_TLfcp_mZr
