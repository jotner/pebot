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
    emb = discord.Embed(title = 'Quote', description = response, color = discord.Colour.nitro_pink())
    await ctx.respond(embed=emb)

# Roll the dice
@bot.command(name = 'roll', description = 'Roll the dice!')
async def deathroll(ctx, value=None):
    if value is None :
        value = 100
    new = random.randint(int(1),int(value))
    emb = discord.Embed(title = 'Roll', description = f"{ctx.author.mention} rolls **{new}** (1-{value})")
    await ctx.respond(embed=emb)

# Save a quote to the quotes.txt file
@bot.command(name = 'savequote', description = 'Save a quote')
async def savequote(ctx, *, quote: str):
    file = open('quotes.txt', 'a')
    file.write(quote)
    file.close()
    emb = discord.Embed(title = 'New quote added!', description = f"Successfully added the quote '*{quote}*'!", color = discord.Colour.green())
    await ctx.respond(embed=emb)

    # channel = bot.get_channel(1062883880618692699)
    # await channel.send(f"{message.author.mention})

bot.run(os.getenv('TOKEN')) # run the bot with the token