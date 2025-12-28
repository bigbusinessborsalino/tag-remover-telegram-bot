 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 65b7a7f651cd9af10bc1d5062aba7cd7d7de9d2e..5619a7fc8b6d613238dd7c5433797a11d7c3c8f6 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,29 @@
-# tag-remover-telegram-bot
\ No newline at end of file
+# tag-remover-telegram-bot
+
+A Telegram bot that re-sends messages to remove the forwarded header, strip `@username` tags from captions/text, and remove embedded link entities so the text appears as plain text.
+
+## Setup
+
+1. Create a bot with [@BotFather](https://t.me/BotFather).
+2. Export your token:
+
+```bash
+export BOT_TOKEN="YOUR_TOKEN"
+```
+
+3. Install dependencies:
+
+```bash
+pip install -r requirements.txt
+```
+
+4. Run the bot:
+
+```bash
+python bot.py
+```
+
+## Notes
+
+- Telegram does not allow programmatically removing visual watermarks that are baked into image/video files. This bot only cleans captions and resends the media to avoid the "Forwarded from" header.
+- The bot re-sends received messages without link entities, so any text that was previously a clickable link becomes plain text.
 
EOF
)
