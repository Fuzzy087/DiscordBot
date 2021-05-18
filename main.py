# Import discord package
import discord
from discord.ext import commands

#Client (bot)
client = commands.Bot(command_prefix='!')

# Bot Functions

# Commands


@client.command(name='bot_version')
async def bot_version(context):

    myEmbed = discord.Embed(
        title='Rando-bot', description='a rando bot to do things', color=0x00ff00)
    myEmbed.add_field(name='Version Code:', value='v1.0', inline=False)
    myEmbed.add_field(name='Date Released', value='Today', inline=True)
    myEmbed.set_footer(text='footer')
    myEmbed.set_author(name='some dude')

    await context.message.channel.send(embed=myEmbed)

# Events


@client.event
async def on_ready():
    general_channel = client.get_channel(788341204394967062)
    await general_channel.send('Bot ready!')


@client.event
async def on_message(message):

    if message.content == 'send a DM':
        await message.author.send('This is a DM! Blah blah blah')

#     if message.content == '!bot_version':
#         general_channel = client.get_channel(788341204394967062)

#         myEmbed = discord.Embed(title='Rando-bot', description='a rando bot to do things', color=0x00ff00)
#         myEmbed.add_field(name='Version Code:', value='v1.0', inline=False)
#         myEmbed.add_field(name='Date Released', value='Today', inline=True)
#         myEmbed.set_footer(text='footer')
#         myEmbed.set_author(name='some dude')

#         await general_channel.send(embed=myEmbed)
#         await client.processs_commands(message)


# Run the client
client.run('$token-here')
