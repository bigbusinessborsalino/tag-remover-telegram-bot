# tag-remover-telegram-bot

A Telegram bot that re-sends messages to remove the forwarded header, strip `@username` tags from captions/text, and remove embedded link entities so the text appears as plain text.

## Setup

1. Create a bot with [@BotFather](https://t.me/BotFather).
2. Export your token:

```bash
export BOT_TOKEN="YOUR_TOKEN"
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the bot:

```bash
python bot.py
```

## Notes

- Telegram does not allow programmatically removing visual watermarks that are baked into image/video files. This bot only cleans captions and resends the media to avoid the "Forwarded from" header.
- The bot re-sends received messages without link entities, so any text that was previously a clickable link becomes plain text.
