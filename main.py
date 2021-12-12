import discord
from discord.ext import commands
import music


cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("OTE2ODE1NzA4MDQwNjA1NzU3.YavpKg.8aSvN-nyZ63K6nRnvQjfNxlI0qU")