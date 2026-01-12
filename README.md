# 📱 TikTok Notifier Discord Bot

A lightweight Discord bot that monitors TikTok RSS feeds and sends a notification to a specific Discord channel whenever a creator posts a new video.

## 🚀 Features
- **RSS-Based Tracking:** No complex TikTok API keys required.
- **Embedded Alerts:** Beautiful Discord embeds including video titles and thumbnails.
- **Multi-Creator Support:** Track as many creators as you like.
- **Auto-Update:** Checks for new content every 5 minutes (customizable).

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- A Discord Bot Token from the [Discord Developer Portal](https://discord.com/developers/applications).
- A host (like [Bot-Hosting.net](https://bot-hosting.net)).

### 2. File Configuration
In your hosting panel's **Files** tab, ensure you have these three files:

#### `bot.py`
Paste your script into this file. Update the `CHANNEL_ID` and `TIKTOK_CREATORS` list at the top of the script.

#### `.env` (Create this file if it doesn't exist)
Add your Discord token here so the bot can log in:
```env
DISCORD_TOKEN=your_token_here_without_quotes