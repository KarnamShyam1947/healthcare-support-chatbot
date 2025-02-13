from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from utils.LLMUtils import analyze_with_query
from utils.FileUtils import markdown_to_text
from datetime import datetime
import os

# Replace with your bot token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Dictionary to store user language preferences
user_language = {}

# Start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("English", callback_data="lang_english")],
        [InlineKeyboardButton("తెలుగు", callback_data="lang_telugu")],
        [InlineKeyboardButton("हिन्दी", callback_data="lang_hindi")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select your language:", reply_markup=reply_markup)

# Callback Query Handler (For Language Selection)
async def language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    language = query.data.split("_")[1]  # Extract language from callback_data
    
    user_language[query.from_user.id] = language  # Store user preference
    await query.answer()
    await query.edit_message_text(f"Language set to {language.capitalize()} ✅\n\nNow you can send text, photos, or audio.")

# Handle Photo Upload
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("handle photo...........")

    user_id = update.message.from_user.id
    lang = user_language.get(user_id, "English")  

    new_file = await update.message.effective_attachment[-1].get_file()
    file = await new_file.download_to_drive(custom_path = f"test_{user_id}.jpg")
    
    print(update.message.caption)
    
    await update.message.reply_text(f"📸 Photo received in {lang}. Now send an audio file or text.")

# Handle Audio Upload
async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("handling audio.........")
    # print(update.message.effective_attachment)
    user_id = update.message.from_user.id
    lang = user_language.get(user_id, "English")  # Get stored language, default to English

    # audio_file = update.message.audio or update.message.voice
    # await audio_file.download_to_drive(f"user_{user_id}_audio.ogg")

    # audio = update.message.audio[-1].get_file()
    # audio.download("user_{user_id}_audio.ogg")
    
    new_file = await update.message.effective_attachment.get_file()
    file = await new_file.download_to_drive(custom_path = f"test_{user_id}.ogg")
    
    
    await update.message.reply_text(f"🎤 Audio received in {lang}. Processing...")

# Handle Text Messages
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = str(update.message.text).lower()
    date_and_time = datetime.now().strftime(' %d-%m-%Y, %H:%M:%S ')
    chat_type = update.message.chat.type
    
    user_id = update.message.from_user.id
    lang = user_language.get(user_id, "English")  # Get stored language, default to English

    user_text = update.message.text
    # response_text = f"📜 You said in {lang}: {user_text}"
    response_text = analyze_with_query(user_text)
    chat_id = update.message.chat.id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    print(f'[{date_and_time}] User {first_name} {last_name} with chat id {chat_id}, send message "{msg}" in {chat_type}')

    response_text = markdown_to_text(response_text)
    
    await update.message.reply_text(response_text)

async def handle_error(update: Update, context):
    print("Error..........")
    
    await update.message.reply_text("error at bot")

# Main Function to Run Bot
def start_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language_selection))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.AUDIO | filters.VOICE, handle_audio))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))  # Text handler

    # app.add_error_handler(handle_error)
    
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    start_bot()
