import discord
import dotenv
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with the token you copied from the Discord Developer Portal
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def purge(ctx, amount: str):
    if amount.lower() == 'all':
        async for message in ctx.channel.history(limit=None):
            if message.author == bot.user:
                await message.delete()
    else:
        try:
            amount = int(amount)
            if amount > 0:
                async for message in ctx.channel.history(limit=amount):
                    if message.author == bot.user:
                        await message.delete()
            else:
                await ctx.send("Please specify a positive number of messages to delete.")
        except ValueError:
            await ctx.send("Invalid amount. Please specify a number or 'all'.")

bot.run('YOUR_BOT_TOKEN')
