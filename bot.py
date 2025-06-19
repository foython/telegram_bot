import logging
import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from asgiref.sync import sync_to_async

# 1. Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telegram_bot.settings")
django.setup()

# 2. Import models AFTER Django setup
from blog.models import TelegramUser
from telegram_bot import settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 3. Use sync_to_async for database operations
@sync_to_async
def get_or_create_user(username):
    return TelegramUser.objects.get_or_create(username=username)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    username = update.effective_user.username
    if username:
        # 4. Call the synchronous DB operation asynchronously
        user, created = await get_or_create_user(username)
        
        if created:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Hello @{username}! Your username has been saved."
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Welcome back @{username}! You're already registered."
            )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You don't have a Telegram username! Please set one first."
        )

if __name__ == '__main__':
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()