import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'[TEST BOT] {bot.user} is ready!')
    print(f'[TEST BOT] Commands: {[cmd.name for cmd in bot.commands]}')

@bot.command(name='test')
async def test_command(ctx):
    print(f"[TEST] Test command from {ctx.author.name}")
    await ctx.reply("Test works!")

@bot.command(name='voice')
async def voice_command(ctx):
    print(f"[VOICE] Command from {ctx.author.name}")
    await ctx.reply("Starting voice connection...")
    
    if not ctx.author.voice:
        await ctx.reply("You need to be in a voice channel!")
        return
    
    channel = ctx.author.voice.channel
    print(f"[VOICE] Connecting to {channel.name}")
    
    try:
        vc = await channel.connect()
        print(f"[VOICE] Connected!")
        await ctx.send("Connected to voice!")
        
        # Wait 10 seconds then disconnect
        await asyncio.sleep(10)
        await vc.disconnect()
        await ctx.send("Disconnected from voice!")
        
    except Exception as e:
        print(f"[VOICE] Error: {e}")
        await ctx.reply(f"Error: {e}")

@bot.event
async def on_message(message):
    if message.content.startswith('!'):
        print(f"[MESSAGE] {message.author.name}: {message.content}")
    await bot.process_commands(message)

bot.run(os.getenv('DISCORD_TOKEN'))
