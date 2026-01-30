# Deployment Guide 🚀

This guide will walk you through deploying your Telegram Media Downloader Bot to Railway.

## Prerequisites

Before you begin, make sure you have:

1. ✅ A Telegram Bot Token (from @BotFather)
2. ✅ A GitHub account
3. ✅ A Railway account ([Sign up here](https://railway.app))
4. ✅ Git installed on your computer

## Step-by-Step Deployment

### Step 1: Create Your Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Start a chat and send: `/newbot`
3. Choose a name for your bot (e.g., "My Media Downloader")
4. Choose a username for your bot (must end in 'bot', e.g., "mymedia_downloader_bot")
5. **IMPORTANT**: Copy the bot token that BotFather gives you (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)
6. Save this token somewhere safe - you'll need it later!

### Step 2: Upload Code to GitHub

1. **Create a new repository on GitHub**:
   - Go to https://github.com/new
   - Name it: `telegram-downloader-bot`
   - Make it Public or Private (your choice)
   - Don't add README, .gitignore, or license (we already have them)
   - Click "Create repository"

2. **Upload your code**:
   
   If you have the files on your computer:
   ```bash
   cd telegram-downloader-bot
   git init
   git add .
   git commit -m "Initial commit: Telegram media downloader bot"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/telegram-downloader-bot.git
   git push -u origin main
   ```
   
   Replace `YOUR_USERNAME` with your GitHub username.

### Step 3: Deploy to Railway

#### Option A: Deploy from GitHub (Recommended)

1. **Login to Railway**:
   - Go to https://railway.app
   - Click "Login" and sign in with GitHub

2. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - If prompted, authorize Railway to access your GitHub

3. **Select Repository**:
   - Find and select `telegram-downloader-bot`
   - Railway will automatically detect the Dockerfile

4. **Add Environment Variable**:
   - Once the project is created, click on your service
   - Go to the "Variables" tab
   - Click "+ New Variable"
   - Add:
     - **Variable name**: `BOT_TOKEN`
     - **Value**: Paste your bot token from Step 1
   - Click "Add"

5. **Deploy**:
   - Railway will automatically start building your bot
   - Wait for the build to complete (usually 2-5 minutes)
   - Check the "Deployments" tab to see the status

6. **Verify Deployment**:
   - Go to the "Logs" tab
   - You should see: "Bot started successfully!"
   - If you see errors, check the troubleshooting section below

#### Option B: Deploy with Railway CLI

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login**:
   ```bash
   railway login
   ```
   This will open a browser window for authentication.

3. **Initialize Project**:
   ```bash
   cd telegram-downloader-bot
   railway init
   ```
   Follow the prompts to create a new project.

4. **Set Environment Variable**:
   ```bash
   railway variables set BOT_TOKEN="your_bot_token_here"
   ```
   Replace with your actual bot token.

5. **Deploy**:
   ```bash
   railway up
   ```

6. **Check Logs**:
   ```bash
   railway logs
   ```

### Step 4: Test Your Bot

1. Open Telegram
2. Search for your bot by username
3. Click "Start" or send `/start`
4. You should see a welcome message!
5. Test with a video link, like:
   ```
   https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

## Troubleshooting 🔧

### Bot not responding

**Check 1**: Verify the bot is running
- Go to Railway dashboard
- Check the "Deployments" tab
- Status should be "Active"

**Check 2**: Check logs for errors
- Go to "Logs" tab in Railway
- Look for error messages
- Common issues:
  - "BOT_TOKEN environment variable is not set!" → Add the BOT_TOKEN variable
  - "Unauthorized" → Check your bot token is correct

**Check 3**: Verify environment variable
- Go to "Variables" tab
- Ensure `BOT_TOKEN` is set
- Value should start with a number and contain a colon

### Build Failed

**Solution 1**: Check Dockerfile
- Ensure Dockerfile is present in the repository
- Verify it's spelled exactly "Dockerfile" (capital D)

**Solution 2**: Check requirements.txt
- Ensure all dependencies are listed
- Verify correct version numbers

### "File too large" errors

**Solution**: 
- Telegram bots have a 50MB limit
- The bot will inform users when files are too large
- Users can try lower quality downloads

### Download errors

**Common causes**:
1. Invalid or private video
2. Geographic restrictions
3. Platform blocking
4. Age-restricted content

**Solutions**:
- Ensure the link is accessible
- Try a different video
- Check if the platform is supported

## Updating Your Bot

When you make changes to your code:

1. **Commit changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```

2. **Railway will automatically redeploy**:
   - No need to do anything else!
   - Railway detects GitHub changes
   - Builds and deploys automatically

## Managing Your Bot

### View Logs
```bash
railway logs
```
or in Railway dashboard → Logs tab

### Restart Bot
Railway dashboard → Your service → Three dots menu → Restart

### Stop Bot
Railway dashboard → Your service → Three dots menu → Remove service

### Monitor Usage
Railway dashboard → Metrics tab
- CPU usage
- Memory usage
- Network traffic

## Cost Information 💰

Railway pricing (as of 2026):
- **Hobby Plan**: $5/month
  - 500 hours of execution time
  - Perfect for this bot
- **Pay-as-you-go**: Available for higher usage

This bot typically uses:
- Low CPU (only active during downloads)
- Low memory (~200-500MB)
- Minimal network (only during downloads)

Expected cost: **$5/month** on Hobby plan

## Security Best Practices 🔒

1. **Never commit your bot token**:
   - Always use environment variables
   - Don't hardcode tokens in code
   - Add `.env` to `.gitignore`

2. **Keep dependencies updated**:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Monitor logs**:
   - Check for suspicious activity
   - Watch for errors

4. **Limit bot access**:
   - Only share bot with trusted users
   - Consider adding user whitelist if needed

## Advanced Configuration

### Custom Domain (Optional)
Railway allows custom domains if you want a webhook URL:
1. Railway dashboard → Settings
2. Add custom domain
3. Update DNS records

### Webhook Mode (Alternative to Polling)
To use webhooks instead of polling:
1. Set up a custom domain
2. Modify bot.py to use webhooks
3. Configure Railway to expose a port

### Multiple Bots
To run multiple bots:
1. Create separate Railway services
2. Each with its own BOT_TOKEN
3. Deploy from the same repository

## Getting Help

If you're stuck:

1. **Check Railway logs** for error messages
2. **Review this guide** for common solutions
3. **Check GitHub Issues** for similar problems
4. **Railway Discord** for platform-specific help

## Next Steps

Once your bot is running:
- ✅ Share it with friends
- ✅ Monitor usage in Railway
- ✅ Customize features in bot.py
- ✅ Add more platforms support
- ✅ Improve error handling

**Congratulations! Your bot is now live! 🎉**
