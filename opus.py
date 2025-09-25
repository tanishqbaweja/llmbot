import discord
try:
    if not discord.opus.is_loaded():
        discord.opus.load_opus('opus')
    print("Opus loaded:", discord.opus.is_loaded())
except Exception as e:
    print("Error loading opus:", e)
