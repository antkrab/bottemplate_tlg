from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters,  MessageHandler


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def echo(update: Update, context) -> None:
    chat_id = update.message.chat_id
    user = update.message.from_user
    text = update.message.text
    print(f"Message from {user.first_name} in group {chat_id}: {text}")
    await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token("<your api key>").build() # build bot by api key

app.add_handler(CommandHandler("hello", hello)) # command /hello -> callback = hello
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo)) #any word -> callback = echo

app.run_polling()