import discord
import os
import random
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="/pebot-help"))
    print(f"{bot.user} is ready and online!")

# Display all bot commands
@bot.command(name = 'pebot-help', description = 'Help commands for Pebot')
async def pebothelp(ctx):
    emb = discord.Embed(title = 'Help Commands', description = f'**/hello** - Say hello to **Pebot**!\n**/roll** - Roll the dice!\n**/quote** - Responds with a random quote from the server\n**/savequote** - Save a quote\n**/pevideos** - Responds with the URL to the TeamPE playlist\n**/wl** - W or L', color = discord.Colour.light_grey())
    await ctx.respond(embed=emb)

# Bot responds with a short message
@bot.command(name = "hello", description = "Say hello to Pebot!")
async def hello(ctx):
    await ctx.respond("Hello! I am Pebot.")

# Roll the dice
@bot.command(name = 'roll', description = 'Roll the dice!')
async def roll(ctx, value=None):
    if value is None :
        value = 100
    result = random.randint(int(1),int(value))
    emb = discord.Embed(title = 'Roll', description = f"{ctx.author.mention} rolls **{result}** (1-{value})")
    await ctx.respond(embed=emb)

# Bot responds with a W or L
@bot.command(name = "wl", description = "W or L")
async def wl(ctx):
    list = ['W', 'L']
    await ctx.respond(f"It's a {random.choice(list)}!")

# Bot responds with a link to the TeamPE playlist
@bot.command(name = "pevideos", description = "Responds with the URL to the TeamPE playlist")
async def pevideos(ctx):
    await ctx.respond("https://www.youtube.com/playlist?list=PL0z7V8OmZj2fFGydcZpCSQzSEEmXSd2DT")

# The server rule is to always respond to the name Alexander with a monkey emoji
@bot.command(name = "alexander", description = "Bootleg Tarzan")
async def alexander(ctx):
    await ctx.respond(":monkey:")    

# Respons with a quote from the server which are stored in the quotes.txt file
@bot.command(name = 'quote', description = 'Responds with a random quote from the server')
async def quote(ctx):
    lines = []
    with open('quotes.txt', 'rt') as qfile:
        for line in qfile:
            lines.append(line)
    response = random.choice(lines)
    emb = discord.Embed(title = 'Quote', description = f"{response}", color = discord.Colour.nitro_pink())
    await ctx.respond(embed=emb)

# Save a quote to TeamPE channel and store it in the quotes.txt file 
@bot.command(name = 'savequote', description = 'Save a quote')
async def savequote(ctx, *, quote: str, name, date=None, time=None):
    file = open('quotes.txt', 'a')
    file.write(quote + '\n')
    file.close()
    channel = 360153117938941953
    if date is None :
        date = ''
    if time is None :
        time = ''
    emb = discord.Embed(title = 'New quote added!', description = f'Successfully added the quote "*{quote}*"!', color = discord.Colour.green())
    await ctx.respond(embed=emb)
    await bot.get_channel(int(channel)).send(f'"{quote}" - {name} {date} {time}')

# Delete the latest quote (NOT IN USE)
# @bot.command(name = 'deletequote', description = 'Delete the latest quote from the random quote file')
# async def deletequote(ctx):
#     file = open('quotes.txt', 'r')
#     lines = file.readlines()
#     lines = lines[:-1]
#     await ctx.respond("Deleted the latest quote.")

bot.run(os.getenv('TOKEN')) # run the bot with the token