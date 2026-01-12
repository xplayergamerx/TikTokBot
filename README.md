\# TikTok Notifier Discord Bot



This bot sends a Discord notification whenever a specified TikTok creator posts a new video.



\## Features



\- Tracks multiple TikTok creators

\- Sends notifications in a Discord channel

\- Includes video title and thumbnail in an embed

\- Checks for new posts every 5 minutes



\## Setup



1\. \*\*Add your bot token as an environment variable on Railway:\*\*



&nbsp;  - Key: `DISCORD\_TOKEN`

&nbsp;  - Value: Your Discord bot token



2\. \*\*Configure `bot.py`:\*\*

&nbsp;  - `CHANNEL\_ID`: The Discord channel where notifications will appear

&nbsp;  - `TIKTOK\_CREATORS`: A list of TikTok usernames to track (without `@`)



3\. \*\*Dependencies:\*\*

&nbsp;  - Listed in `requirements.txt` (`discord.py`, `feedparser`)



4\. \*\*Deploy on Railway:\*\*

&nbsp;  - Connect your GitHub repo

&nbsp;  - Railway will automatically install dependencies and run `bot.py`



\## Notes



\- Make sure the bot has \*\*Send Messages\*\* and \*\*Embed Links\*\* permissions in the target Discord channel.

\- TikTok usernames must be \*\*exact and case-sensitive\*\*.

\- The free Railway plan may sleep after periods of inactivity, but the bot will restart when needed.

