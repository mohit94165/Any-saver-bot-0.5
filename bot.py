import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello bhai! Video link bhej (YouTube, Insta, TikTok etc.). "
        "Ab cookies ke saath restricted videos bhi try kar sakte hain. Short videos best!"
    )

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'video.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'continuedl': True,
        'noplaylist': True,  # Sirf ek video
    }

    # Cookies add karo agar variable mein hai
    cookies_content = os.getenv("COOKIES_CONTENT")
    if cookies_content:
        cookies_path = '/tmp/youtube_cookies.txt'
        try:
            with open(cookies_path, 'w', encoding='utf-8') as f:
                f.write(cookies_content)
            ydl_opts['cookiefile'] = cookies_path
            logger.info("Cookies use kiye gaye!")
        except Exception as e:
            logger.error(f"Cookies file banane mein gadbad: {e}")

    # Extra safe: User agent browser jaisa
    ydl_opts['useragent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if not filename.endswith('.mp4'):
                filename = filename.rsplit('.', 1)[0] + '.mp4'
        return filename
    except Exception as e:
        raise Exception(f"Download fail: {str(e)}")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.startswith('http'):
        await update.message.reply_text("Download shuru... 30 sec - 2 min wait kar bhai!")
        try:
            filename = download_video(text)
            file_size_mb = os.path.getsize(filename) / (1024 * 1024)
            if file_size_mb > 48:
                await update.message.reply_text(f"Video bada hai ({file_size_mb:.1f} MB). Bot 50MB tak hi bhej sakta hai. Chhota try kar!")
                os.remove(filename)
                return

            with open(filename, 'rb') as video:
                await update.message.reply_video(video=video, supports_streaming=True)
            await update.message.reply_text("Video aa gaya! Mazaa aaya? 😎")
            os.remove(filename)
        except Exception as e:
            error_str = str(e)
            logger.error(error_str)
            if "not a bot" in error_str.lower() or "sign in" in error_str.lower():
                await update.message.reply_text("YouTube ne bot samjha! Cookies sahi daale? Ya normal public video try kar (restricted mat bhej abhi).")
            else:
                await update.message.reply_text(f"Error: {error_str[:200]}... Link check kar ya dusra video try kar.")
    else:
        await update.message.reply_text("Valid link bhej na bhai (http ya https se start ho).")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable nahi mila!")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    print("Bot start ho gaya!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
