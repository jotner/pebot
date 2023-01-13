import discord
import os
import random
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    print(f"{bot.user} is ready and online!")

@bot.command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hello! I am Pebot.")

@bot.command(name = "alexander", description = "Bootleg Tarzan")
async def alexander(ctx):
    await ctx.respond(":monkey:")    

# Random quotes from the server
@bot.command(name = 'quote', description = 'Responds with a random quote from the server')
async def quote(ctx):
    mylines = []
    with open('quotes.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)

    response = random.choice(mylines)
    emb = discord.Embed(title = 'Quote', description = f"{response}", color = discord.Colour.nitro_pink())
    await ctx.respond(embed=emb)

# Roll the dice
@bot.command(name = 'roll', description = 'Roll the dice!')
async def roll(ctx, value=None):
    if value is None :
        value = 100
    new = random.randint(int(1),int(value))
    emb = discord.Embed(title = 'Roll', description = f"{ctx.author.mention} rolls **{new}** (1-{value})")
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

# Delete the latest quote
# @bot.command(name = 'deletequote', description = 'Delete the latest quote from the random quote file')
# async def deletequote(ctx):
#     file = open('quotes.txt', 'r')
#     lines = file.readlines()
#     lines = lines[:-1]
#     await ctx.respond("Deleted the latest quote.")

bot.run(os.getenv('TOKEN')) # run the bot with the token