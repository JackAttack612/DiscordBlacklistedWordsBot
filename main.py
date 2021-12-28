# Imports DON'T TOUCH UNLESS YOU ARE ADDING ONTO BOT
import nextcord
from nextcord.ext import commands

# DONT EDIT UNLESS YOU KNOW WHAT YOU ARE DOING
intents = nextcord.Intents.default()
intents.members = True

client = nextcord.Client()
client.remove_command("help")

# Put your discord bot token here
TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"

# Replace whats inside "" with the words you want to be blacklisted
blacklist_words = ["BlacklistedWordHere", "BlacklistedWordHere2", "BlacklistedWordHere3"]

@client.event
async def on_message(message):
    msg = message.content
    if any(word in msg for word in blacklist_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} You used a word that was blacklisted! Your message has been deleted.")
        
        # Logging Message
        # Change YourChannelID to the channel you want the log to be sent in
        channel = client.get_channel(YOUR_DISCORD_CHANNEL_ID_HERE)
        embed = nextcord.Embed(title=f"{message.author.name}#{message.author.discriminator} used a blacklisted word!",description=f"Message: {message.content}", color=0x5e008c)
        embed.set_footer(text=f'ID: {message.author.id}', icon_url=message.author.avatar.url)
        embed.set_thumbnail(url=message.author.avatar.url)
        await channel.send(embed=embed)

client.run(TOKEN)