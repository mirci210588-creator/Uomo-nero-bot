from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = '8262965257:AAGH14J43KYwBexihGhxL_gdAn6RW1DRnlo'

async def start(update, context):
await update.message.reply_text("Il bot dell'Uomo Nero è online!")

async def partecipa(update, context):
await update.message.reply_text("Sei stato aggiunto alla partita.")

async def gioca(update, context):
await update.message.reply_text("Distribuzione in corso...")

if name == 'main':
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("partecipa", partecipa))
app.add_handler(CommandHandler("gioca", gioca))
print("Bot pronto!")
app.run_polling()