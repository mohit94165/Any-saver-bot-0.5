# 🚀 QUICK START GUIDE - Telegram Media Downloader Bot

## ✅ What You Have

A fully functional Telegram bot that downloads:
- 📹 Videos (YouTube, Instagram, TikTok, Twitter, Facebook, etc.)
- 🎵 Audio/MP3 (extracts from videos)
- 🖼️ Images (from direct links)

## 🎯 5-Minute Setup

### Step 1: Get Your Bot Token (2 minutes)

1. Open Telegram, search: **@BotFather**
2. Send: `/newbot`
3. Follow prompts to name your bot
4. **COPY THE TOKEN** (looks like: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)
5. Keep it safe!

### Step 2: Upload to GitHub (2 minutes)

```bash
# Navigate to the bot folder
cd telegram-downloader-bot

# Initialize git
git init
git add .
git commit -m "Initial commit"

# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Railway (1 minute)

1. Go to: https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository
5. Click your service → **"Variables"** tab
6. Add variable:
   - Name: `BOT_TOKEN`
   - Value: *paste your token*
7. Click **"Add"**

**Done!** Railway will build and deploy automatically.

### Step 4: Test Your Bot

1. Open Telegram
2. Search for your bot username
3. Send: `/start`
4. Try sending a YouTube link!

## 📝 Example Usage

**Download Video:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**Download Audio/MP3:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ audio
```

**Download Image:**
```
https://example.com/image.jpg
```

## 🎯 Supported Platforms

✅ YouTube
✅ Instagram  
✅ Twitter/X
✅ TikTok
✅ Facebook
✅ Reddit
✅ Vimeo
✅ Dailymotion
✅ Twitch
✅ 1000+ more sites!

## ⚙️ How It Works

1. You send a link to the bot
2. Bot detects media type (video/audio/image)
3. Downloads using yt-dlp (industry standard)
4. Converts to MP3 if audio requested
5. Sends file back to you
6. Deletes temporary files (no storage)

## 🔒 Privacy & Security

- ✅ No data stored
- ✅ Temporary files deleted immediately
- ✅ No user tracking
- ✅ Open source code

## ⚠️ Limitations

- Maximum file size: **50MB** (Telegram API limit)
- Some platforms may block downloads
- Geographic restrictions may apply
- Respects copyright and terms of service

## 🛠️ Troubleshooting

### Bot not responding?
1. Check Railway dashboard - is it running?
2. Check Variables - is BOT_TOKEN set correctly?
3. Check Logs for errors

### Download failed?
1. Is the link valid and public?
2. Try a different video
3. Check if platform is supported

### File too large?
- Telegram bots can only send files up to 50MB
- Try a different video or lower quality

## 📊 Railway Dashboard

Monitor your bot:
- **Deployments**: Check if running
- **Logs**: See real-time activity
- **Metrics**: CPU/Memory usage
- **Variables**: Manage BOT_TOKEN

## 💰 Cost

Railway Hobby Plan: **$5/month**
- 500 hours execution time
- More than enough for this bot
- First $5 included with trial

## 🔄 Update Your Bot

After making code changes:
```bash
git add .
git commit -m "Update description"
git push
```
Railway auto-deploys!

## 📚 Files Included

- `bot.py` - Main bot code
- `requirements.txt` - Dependencies
- `Dockerfile` - Container setup
- `railway.json` - Railway config
- `README.md` - Full documentation
- `DEPLOYMENT.md` - Detailed guide
- `.gitignore` - Git configuration

## 🎉 You're All Set!

Your bot is production-ready with:
- ✅ Robust error handling
- ✅ Clean code
- ✅ Auto file cleanup
- ✅ Multi-platform support
- ✅ User-friendly messages
- ✅ No fake features
- ✅ Industry-standard tools

## 💡 Pro Tips

1. **Share responsibly** - Don't overload the bot
2. **Monitor logs** - Check Railway dashboard regularly
3. **Update dependencies** - Keep yt-dlp updated
4. **Backup token** - Save your BOT_TOKEN securely
5. **Read docs** - Check README.md for advanced features

## 🆘 Need Help?

1. Check `DEPLOYMENT.md` for detailed steps
2. Check `README.md` for full documentation
3. Review Railway logs for errors
4. Check Telegram @BotFather if token issues

---

**Ready to deploy? Follow Steps 1-4 above!** 🚀

**Questions?** All documentation is in the repository.

**Happy downloading!** 🎬🎵📷
