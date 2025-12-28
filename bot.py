codex/create-telegram-bot-to-format-messages
import os
import re
from typing import Optional

from telegram import Message, Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters


USERNAME_RE = re.compile(r"@\w+")
EXTRA_SPACE_RE = re.compile(r"\s{2,}")
URL_RE = re.compile(r"(?:https?://|www\.)\S+", re.IGNORECASE)


def _neutralize_url(match: re.Match[str]) -> str:
    url = match.group(0)
    return url.replace(".", ".\u200b")


def clean_text(text: str) -> str:
    cleaned = USERNAME_RE.sub("", text)
    cleaned = URL_RE.sub(_neutralize_url, cleaned)
    cleaned = EXTRA_SPACE_RE.sub(" ", cleaned)
    return cleaned.strip()


def get_caption(message: Message) -> Optional[str]:
    if message.caption:
        return clean_text(message.caption)
    if message.text:
        return clean_text(message.text)
    return None


async def resend_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if not message:
        return

    caption = get_caption(message)
    chat_id = message.chat_id

    if message.photo:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=message.photo[-1].file_id,
            caption=caption,
        )
        return

    if message.video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=message.video.file_id,
            caption=caption,
        )
        return

    if message.document:
        await context.bot.send_document(
            chat_id=chat_id,
            document=message.document.file_id,
            caption=caption,
        )
        return

    if message.audio:
        await context.bot.send_audio(
            chat_id=chat_id,
            audio=message.audio.file_id,
            caption=caption,
        )
        return

    if message.animation:
        await context.bot.send_animation(
            chat_id=chat_id,
            animation=message.animation.file_id,
            caption=caption,
        )
        return

    if message.voice:
        await context.bot.send_voice(
            chat_id=chat_id,
            voice=message.voice.file_id,
            caption=caption,
        )
        return

    if message.text:
        await context.bot.send_message(chat_id=chat_id, text=caption or "")


def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable is required")

    application = Application.builder().token(token).build()

    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, resend_message))
    application.run_polling()


if __name__ == "__main__":
    main()
======
 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/bot.py b/bot.py
new file mode 100644
index 0000000000000000000000000000000000000000..cbb0de6a8a37664deade8a35c498d0ac9389b706
--- /dev/null
+++ b/bot.py
@@ -0,0 +1,99 @@
+import os
+import re
+from typing import Optional
+
+from telegram import Message, Update
+from telegram.ext import Application, ContextTypes, MessageHandler, filters
+
+
+USERNAME_RE = re.compile(r"@\w+")
+EXTRA_SPACE_RE = re.compile(r"\s{2,}")
+
+
+def clean_text(text: str) -> str:
+    cleaned = USERNAME_RE.sub("", text)
+    cleaned = EXTRA_SPACE_RE.sub(" ", cleaned)
+    return cleaned.strip()
+
+
+def get_caption(message: Message) -> Optional[str]:
+    if message.caption:
+        return clean_text(message.caption)
+    if message.text:
+        return clean_text(message.text)
+    return None
+
+
+async def resend_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
+    message = update.effective_message
+    if not message:
+        return
+
+    caption = get_caption(message)
+    chat_id = message.chat_id
+
+    if message.photo:
+        await context.bot.send_photo(
+            chat_id=chat_id,
+            photo=message.photo[-1].file_id,
+            caption=caption,
+        )
+        return
+
+    if message.video:
+        await context.bot.send_video(
+            chat_id=chat_id,
+            video=message.video.file_id,
+            caption=caption,
+        )
+        return
+
+    if message.document:
+        await context.bot.send_document(
+            chat_id=chat_id,
+            document=message.document.file_id,
+            caption=caption,
+        )
+        return
+
+    if message.audio:
+        await context.bot.send_audio(
+            chat_id=chat_id,
+            audio=message.audio.file_id,
+            caption=caption,
+        )
+        return
+
+    if message.animation:
+        await context.bot.send_animation(
+            chat_id=chat_id,
+            animation=message.animation.file_id,
+            caption=caption,
+        )
+        return
+
+    if message.voice:
+        await context.bot.send_voice(
+            chat_id=chat_id,
+            voice=message.voice.file_id,
+            caption=caption,
+        )
+        return
+
+    if message.text:
+        await context.bot.send_message(chat_id=chat_id, text=caption or "")
+
+
+def main() -> None:
+    token = os.environ.get("BOT_TOKEN")
+    if not token:
+        raise RuntimeError("BOT_TOKEN environment variable is required")
+
+    application = Application.builder().token(token).build()
+
+    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, resend_message))
+    application.run_polling()
+
+
+if __name__ == "__main__":
+    main()
 
EOF
)
main
