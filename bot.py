import discord
from discord.ext import tasks
import feedparser
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# -------- CONFIGURATION --------
CHANNEL_ID = 1460294826212720791           
TIKTOK_CREATORS = ["mrbreakthebar"]  
CHECK_INTERVAL = 5                         
TOKEN = os.getenv("DISCORD_TOKEN")
# --------------------------------

# We need message_content to hear !test and default for everything else
intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

# Keep track of last post for each creator
last_posts = {creator: None for creator in TIKTOK_CREATORS}

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')
    print(f'📺 Tracking creators: {", ".join(TIKTOK_CREATORS)}')
    if not check_tiktok.is_running():
        check_tiktok.start()

# --- TEST COMMAND ---
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!test":
        await message.channel.send("✅ **Bot is Online!** I am successfully reading the .env file and have permission to post here.")
        print(f"Test command handled in #{message.channel}")

@tasks.loop(minutes=CHECK_INTERVAL)
async def check_tiktok():
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"❌ Error: Cannot find channel {CHANNEL_ID}. Check the ID and Bot Permissions!")
        return

    for creator in TIKTOK_CREATORS:
        rss_url = f'https://www.tiktok.com/@{creator}/feed'
        feed = feedparser.parse(rss_url)
        
        if not feed.entries:
            continue
            
        latest = feed.entries[0]

        # If this post is new, send notification
        if last_posts.get(creator) != latest.id:
            # Update the tracker
            last_posts[creator] = latest.id
            
            embed = discord.Embed(
                title=f"New TikTok by @{creator}",
                url=latest.link,
                description=latest.get('title', 'No description'),
                color=0x00ff00
            )
            
            if "media_thumbnail" in latest:
                embed.set_thumbnail(url=latest.media_thumbnail[0]['url'])
            
            # This line sends the @everyone alert followed by the embed
            await channel.send(content="@everyone 📢 New TikTok post!", embed=embed)
            print(f"🚀 Sent notification for {creator}")

if TOKEN:
    client.run(TOKEN)
else:
    print("❌ ERROR: No token found! Check your .env file on Bot-Hosting.")