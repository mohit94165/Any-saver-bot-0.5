import os
import logging
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
import requests
from urllib.parse import urlparse
import tempfile

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    welcome_message = """
🎬 **Welcome to Media Downloader Bot!** 🎵

I can download:
✅ Videos from YouTube, Instagram, Twitter, TikTok, Facebook, and more
✅ Images from direct links
✅ Audio/MP3 from YouTube and other platforms

**How to use:**
Just send me any video/audio/image link!

**Commands:**
/start - Show this message
/help - Get help

**Supported platforms:**
YouTube, Instagram, Twitter/X, TikTok, Facebook, Reddit, Vimeo, Dailymotion, and many more!
    """
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = """
📖 **Help & Instructions**

**Supported Media Types:**
• Videos (MP4, WebM, etc.)
• Audio (MP3, M4A, etc.)
• Images (JPG, PNG, GIF, etc.)

**How to download:**
1. Find a video/audio/image link
2. Send it to me
3. Wait for processing
4. Receive your file!

**Tips:**
• Send direct links for best results
• For audio, I'll automatically extract MP3
• Large files may take longer to process

**Examples:**
• YouTube: https://youtube.com/watch?v=...
• Instagram: https://instagram.com/p/...
• Twitter: https://twitter.com/.../status/...
• Direct image: https://example.com/image.jpg
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

def is_valid_url(url):
    """Check if the string is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def is_image_url(url):
    """Check if URL points to an image."""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg']
    parsed = urlparse(url)
    path = parsed.path.lower()
    return any(path.endswith(ext) for ext in image_extensions)

async def download_image(url, update: Update):
    """Download and send image."""
    try:
        response = requests.get(url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            temp_file.write(response.content)
            temp_path = temp_file.name
        
        # Send image
        with open(temp_path, 'rb') as photo:
            await update.message.reply_photo(photo=photo, caption="✅ Image downloaded successfully!")
        
        # Clean up
        os.unlink(temp_path)
        return True
    except Exception as e:
        logger.error(f"Image download error: {e}")
        return False

async def download_media(url, update: Update, download_type='video'):
    """Download video or audio using yt-dlp."""
    try:
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Configure yt-dlp options
        if download_type == 'audio':
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
            }
        else:
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
                'merge_output_format': 'mp4',
            }
        
        # Download the media
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            # Find the downloaded file
            downloaded_file = None
            for file in os.listdir(temp_dir):
                if download_type == 'audio' and file.endswith('.mp3'):
                    downloaded_file = os.path.join(temp_dir, file)
                    break
                elif download_type == 'video' and (file.endswith('.mp4') or file.endswith('.webm') or file.endswith('.mkv')):
                    downloaded_file = os.path.join(temp_dir, file)
                    break
            
            if not downloaded_file:
                # Fallback: take first file
                files = os.listdir(temp_dir)
                if files:
                    downloaded_file = os.path.join(temp_dir, files[0])
            
            if downloaded_file and os.path.exists(downloaded_file):
                file_size = os.path.getsize(downloaded_file)
                
                # Telegram has a 50MB limit for bots
                if file_size > 50 * 1024 * 1024:
                    await update.message.reply_text(
                        "❌ File is too large (>50MB). Telegram bots have a 50MB upload limit."
                    )
                    return False
                
                # Send the file
                caption = f"✅ {download_type.capitalize()} downloaded successfully!"
                if 'title' in info:
                    caption += f"\n📝 Title: {info['title'][:100]}"
                
                with open(downloaded_file, 'rb') as media:
                    if download_type == 'audio':
                        await update.message.reply_audio(
                            audio=media,
                            caption=caption,
                            title=info.get('title', 'Downloaded Audio')[:100],
                            performer=info.get('uploader', 'Unknown')[:100]
                        )
                    else:
                        await update.message.reply_video(
                            video=media,
                            caption=caption,
                            supports_streaming=True
                        )
                
                # Clean up
                os.unlink(downloaded_file)
                os.rmdir(temp_dir)
                return True
            else:
                await update.message.reply_text("❌ Failed to locate downloaded file.")
                return False
                
    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Download error: {e}")
        await update.message.reply_text(
            f"❌ Download failed. The link might be invalid or the platform is not supported.\n\n"
            f"Error: {str(e)[:200]}"
        )
        return False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await update.message.reply_text(f"❌ An error occurred: {str(e)[:200]}")
        return False
    finally:
        # Clean up temp directory if it still exists
        try:
            if os.path.exists(temp_dir):
                for file in os.listdir(temp_dir):
                    os.unlink(os.path.join(temp_dir, file))
                os.rmdir(temp_dir)
        except:
            pass

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages with URLs."""
    message_text = update.message.text
    
    # Extract URLs from message
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    urls = url_pattern.findall(message_text)
    
    if not urls:
        await update.message.reply_text(
            "❌ No valid URL found. Please send me a link to a video, audio, or image!"
        )
        return
    
    url = urls[0]  # Process first URL
    
    if not is_valid_url(url):
        await update.message.reply_text("❌ Invalid URL. Please check and try again.")
        return
    
    # Send processing message
    processing_msg = await update.message.reply_text("⏳ Processing your link...")
    
    try:
        # Check if it's an image
        if is_image_url(url):
            success = await download_image(url, update)
            if success:
                await processing_msg.delete()
            else:
                await processing_msg.edit_text("❌ Failed to download image. Please try a different link.")
            return
        
        # Try to determine if user wants audio or video
        message_lower = message_text.lower()
        wants_audio = any(keyword in message_lower for keyword in ['audio', 'mp3', 'song', 'music'])
        
        # Try downloading as video first, then audio if requested
        if wants_audio:
            await processing_msg.edit_text("🎵 Downloading audio...")
            success = await download_media(url, update, 'audio')
        else:
            await processing_msg.edit_text("🎬 Downloading video...")
            success = await download_media(url, update, 'video')
        
        if success:
            await processing_msg.delete()
        else:
            # If video failed and audio wasn't tried, try audio
            if not wants_audio:
                await processing_msg.edit_text("🎵 Trying to download as audio...")
                success = await download_media(url, update, 'audio')
                if success:
                    await processing_msg.delete()
    
    except Exception as e:
        logger.error(f"Handler error: {e}")
        await processing_msg.edit_text(f"❌ An error occurred: {str(e)[:200]}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")
    
    if update and update.message:
        await update.message.reply_text(
            "❌ An unexpected error occurred. Please try again later."
        )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Bot started successfully!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
