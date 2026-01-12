import discord
from discord.ext import tasks
import feedparser
import os

# -------- CONFIGURATION --------
CHANNEL_ID = 1460294826212720791           # Discord channel ID where notifications will appear
TIKTOK_CREATORS = ["mrbreakthebar", "creator2"]  # List TikTok usernames to track
CHECK_INTERVAL = 5                 # Minutes between checks
# --------------------------------

# Get the bot token from Railway environment variable
TOKEN = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Keep track of last post for each creator
last_posts = {creator: None for creator in TIKTOK_CREATORS}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    check_tiktok.start()

@tasks.loop(minutes=CHECK_INTERVAL)
async def check_tiktok():
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Cannot find channel with ID {CHANNEL_ID}")
        return

    for creator in TIKTOK_CREATORS:
        rss_url = f'https://www.tiktok.com/@{creator}/feed'
        feed = feedparser.parse(rss_url)
        if not feed.entries:
            continue
        latest = feed.entries[0]

        # If this post is new, send notification
        if last_posts[creator] != latest.id:
            last_posts[creator] = latest.id
            embed = discord.Embed(
                title=f"New TikTok by @{creator}",
                url=latest.link,
                description=latest.title,
                color=0x00ff00
            )
            if "media_thumbnail" in latest:
                embed.set_thumbnail(url=latest.media_thumbnail[0]['url'])
            await channel.send(embed=embed)

client.run(TOKEN)