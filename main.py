from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "YOUR_BOT_TOKEN_HERE"

def start(update, context):
    update.message.reply_text("Mmm... you’ve awakened me 😈")

def handle_message(update, context):
    user = update.message.from_user.first_name
    text = update.message.text.lower()

    if "hi" in text or "hey" in text:
        update.message.reply_text(f"Hey {user} 😘 I was waiting for you.")
    elif "love" in text:
        update.message.reply_text("Don't play with my heart, baby 💋")
    elif "shannel" in text:
        update.message.reply_text("You called me, Daddy? 😏")
    else:
        update.message.reply_text("Say more... I like that 😈")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
print("Shannel is live 😘")
updater.idle()