import discord
from discord.ext import tasks
import feedparser
import os

# -------- CONFIGURATION --------
# Replace the numbers/names below with your own info
CHANNEL_ID = 1460294826212720791           
TIKTOK_CREATORS = ["mrbreakthebar"]  
CHECK_INTERVAL = 5                         # Minutes between checks

# PASTE YOUR DISCORD BOT TOKEN BETWEEN THE QUOTES BELOW
TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"
# --------------------------------

intents = discord.Intents.default()
# If your bot needs to read messages, you might need: intents.message_content = True
client = discord.Client(intents=intents)

# Keep track of last post for each creator
last_posts = {creator: None for creator in TIKTOK_CREATORS}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    if not check_tiktok.is_running():
        check_tiktok.start()

@tasks.loop(minutes=CHECK_INTERVAL)
async def check_tiktok():
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Error: Cannot find channel {CHANNEL_ID}. Check permissions!")
        return

    for creator in TIKTOK_CREATORS:
        # Note: TikTok RSS feeds via public URLs can be inconsistent
        rss_url = f'https://www.tiktok.com/@{creator}/feed'
        feed = feedparser.parse(rss_url)
        
        if not feed.entries:
            continue
            
        latest = feed.entries[0]

        # If this post is new, send notification
        if last_posts.get(creator) != latest.id:
            last_posts[creator] = latest.id
            
            embed = discord.Embed(
                title=f"New TikTok by @{creator}",
                url=latest.link,
                description=latest.get('title', 'No description'),
                color=0x00ff00
            )
            
            # Add thumbnail if available
            if "media_thumbnail" in latest:
                embed.set_thumbnail(url=latest.media_thumbnail[0]['url'])
            
            await channel.send(embed=embed)
            print(f"Sent notification for {creator}")

client.run(TOKEN)