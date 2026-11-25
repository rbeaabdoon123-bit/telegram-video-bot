from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "9063389269:AAHvZP5Uc_bBwJjXv8_5yAWfJ9icDlRy81o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك 🤖\n"
        "أرسل رابط فيديو وسأتحقق من صيغة الرابط.\n"
        "هذا البوت لا يستخرج الفيديوهات من مواقع محمية."
    )

async def check_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text.strip()

    if not link.startswith(("https://", "http://")):
        await update.message.reply_text("أرسل رابطاً يبدأ بـ https://")
        return

    await update.message.reply_text(
        "وصلني الرابط بنجاح ✅\n"
        "يمكن استخدام روابط الملفات المباشرة المسموح بها "
        "في نظام معالجة الفيديو."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_link))

app.run_polling()
