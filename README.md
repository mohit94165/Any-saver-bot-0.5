# Telegram Media Downloader Bot 🎬🎵📷

A powerful Telegram bot that downloads videos, audio (MP3), and images from various platforms including YouTube, Instagram, Twitter, TikTok, Facebook, and more!

## Features ✨

- **Video Downloads**: Download videos from YouTube, Instagram, Twitter/X, TikTok, Facebook, Reddit, Vimeo, and 1000+ other sites
- **Audio Downloads**: Extract and download audio as MP3 from videos
- **Image Downloads**: Download images from direct links
- **Multi-Platform Support**: Works with most popular video/social media platforms
- **High Quality**: Downloads best available quality
- **User Friendly**: Simple interface - just send a link!
- **Error Handling**: Robust error handling with informative messages

## Supported Platforms 🌐

- YouTube
- Instagram
- Twitter/X
- TikTok
- Facebook
- Reddit
- Vimeo
- Dailymotion
- Twitch
- And 1000+ more sites supported by yt-dlp!

## Prerequisites 📋

- Python 3.11+
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Railway account (for deployment) or any other hosting platform

## Quick Start 🚀

### 1. Get Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token provided

### 2. Local Testing (Optional)

```bash
# Clone the repository
git clone <your-repo-url>
cd telegram-downloader-bot

# Install dependencies
pip install -r requirements.txt

# Set your bot token
export BOT_TOKEN="your_bot_token_here"

# Run the bot
python bot.py
```

### 3. Deploy to Railway 🚂

#### Method 1: Deploy from GitHub (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Railway**:
   - Go to [Railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect the Dockerfile

3. **Set Environment Variable**:
   - In your Railway project, go to "Variables"
   - Add a new variable:
     - Key: `BOT_TOKEN`
     - Value: Your bot token from BotFather
   - Click "Add"

4. **Deploy**:
   - Railway will automatically build and deploy your bot
   - Check the deployment logs to ensure it started successfully

#### Method 2: Deploy with Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Add environment variable
railway variables set BOT_TOKEN="your_bot_token_here"

# Deploy
railway up
```

### 4. Using Your Bot 🤖

1. Open Telegram and search for your bot by username
2. Send `/start` to see the welcome message
3. Send any video/audio/image link
4. Wait for the bot to process and download
5. Receive your media file!

## Bot Commands 📝

- `/start` - Show welcome message and features
- `/help` - Display help information

## Usage Examples 💡

### Download a YouTube Video
```
Send: https://youtube.com/watch?v=dQw4w9WgXcQ
Bot will download and send the video
```

### Download Audio/MP3
```
Send: https://youtube.com/watch?v=dQw4w9WgXcQ audio
Or: https://youtube.com/watch?v=dQw4w9WgXcQ mp3
Bot will extract and send MP3 file
```

### Download an Image
```
Send: https://example.com/image.jpg
Bot will download and send the image
```

## Configuration ⚙️

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Your Telegram bot token from BotFather | Yes |

### Limitations

- Maximum file size: 50MB (Telegram bot API limit)
- Supported formats: MP4, WebM, MP3, JPG, PNG, GIF, etc.
- Some platforms may have download restrictions

## Troubleshooting 🔧

### Bot not responding
- Check if the bot is running in Railway dashboard
- Verify `BOT_TOKEN` environment variable is set correctly
- Check Railway logs for errors

### Download failed
- Ensure the link is valid and accessible
- Some platforms may block downloads
- Check if the video/audio is available in your region

### File too large error
- Telegram bots can only send files up to 50MB
- Try downloading a lower quality version

## Project Structure 📁

```
telegram-downloader-bot/
├── bot.py              # Main bot code
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── railway.json       # Railway deployment config
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## Technical Details 🔍

### Dependencies

- **python-telegram-bot**: Telegram Bot API wrapper
- **yt-dlp**: Universal video downloader
- **requests**: HTTP library for image downloads
- **ffmpeg**: Audio/video processing (included in Docker)

### How It Works

1. User sends a link to the bot
2. Bot detects the type of media (video/audio/image)
3. For videos/audio: Uses yt-dlp to download
4. For images: Uses requests library
5. Processes and converts if needed (e.g., to MP3)
6. Sends the file back to the user

## Security & Privacy 🔒

- No data is stored permanently
- All downloads are temporary and deleted after sending
- No user data is collected or logged
- Downloads happen in isolated temporary directories

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License 📄

This project is open source and available under the MIT License.

## Support 💬

If you encounter any issues:
1. Check the troubleshooting section
2. Review Railway deployment logs
3. Ensure all dependencies are installed
4. Verify your bot token is correct

## Acknowledgments 🙏

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the amazing download engine
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the Telegram API wrapper
- [Railway](https://railway.app) for easy deployment

## Disclaimer ⚠️

This bot is for educational purposes. Make sure you have the right to download content and respect copyright laws and platform terms of service.

---

**Enjoy your Media Downloader Bot! 🎉**
