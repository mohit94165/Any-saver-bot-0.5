import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp

# Logging for debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello bhai! Video ka share link bhej do (YouTube, Insta, TikTok, FB etc.), "
        "main download karke bhej dunga. Short videos best chalte hain (50MB tak)."
    )

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'video.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'continuedl': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        # Agar mp4 nahi mila to force mp4
        if not filename.endswith('.mp4'):
            filename = filename.rsplit('.', 1)[0] + '.mp4'
    return filename

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.startswith('http'):
        await update.message.reply_text("Video download ho raha hai... 1-2 min wait kar bhai!")
        try:
            filename = download_video(text)
            file_size = os.path.getsize(filename) / (1024 * 1024)  # MB mein
            if file_size > 48:  # 50MB se thoda kam safe
                await update.message.reply_text(
                    f"Video bada hai ({file_size:.1f} MB). Bot sirf 50MB tak bhej sakta hai. "
                    "Chhota video try kar ya premium features ke liye baad mein fix karenge."
                )
                os.remove(filename)
                return

            with open(filename, 'rb') as video:
                await update.message.reply_video(video=video, supports_streaming=True)
            await update.message.reply_text("Ho gaya! Video mil gaya? 😎")
            os.remove(filename)  # Clean up
        except Exception as e:
            logger.error(f"Error: {e}")
            await update.message.reply_text(f"Kuch gadbad ho gayi: {str(e)}\nLink check kar ya alag site try kar.")
    else:
        await update.message.reply_text("Bhai valid video link bhej na (http/https se shuru ho).")

def main():
    # Railway pe variable set karna, yahan mat daal
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("BOT_TOKEN nahi mila environment se!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    print("Bot chal raha hai...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
