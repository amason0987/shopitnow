from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

BOT_TOKEN = "7617274250:AAHc8n-oHyGXIrSQQj12OVXff57Bh9ygtqY"

# Dictionary of subjects and Drive links
file_links = {
    "Physics": {
        "WEP": "https://drive.google.com/file/d/19dB8BJZC2RBql_f539x48_KxrtrdRRv0/view?usp=drivesdk",
        "NLM": "https://drive.google.com/file/d/19cLEzFkJhJ90jMaNRgSicURkUFN3pnD4/view?usp=drivesdk",
        "Rotation": "https://drive.google.com/file/d/192slBwvb29KZDHAnmjy-JwfapzL6POaC/view?usp=drivesdk",
        "Motion": "https://drive.google.com/file/d/19WbvuOQgI84ud5DIaBd6D-QPkw1JPe2V/view?usp=drivesdk",
        "Motion In StLn": "https://drive.google.com/file/d/19QQBK-koZMO39CuNFJ5YQyk7U8xY0pHZ/view?usp=drivesdk"
    },
    "Chemistry": {
        "ChemBonding": "https://drive.google.com/file/d/19P4aynx_NygQZVoIVciYmNwnZKVlsmOP/view?usp=drivesdk",
        "Eqm": "https://drive.google.com/file/d/19PUgSINM7vR9pePzOSxm8B4JwpwYjq1c/view?usp=drivesdk",
        "ThermoD": "https://drive.google.com/file/d/197GgUY7OZwL4XsRklInp2ZIfOqOpscOT/view?usp=drivesdk",
        "OC": "https://drive.google.com/file/d/19B4DDnKwXt-6BatpgZfT5LW0vW61VX8D/view?usp=drivesdk",
        "HydroC": "https://drive.google.com/file/d/19AMVO1lB64NSrKqVoxlgjS_pSpPkZbtg/view?usp=drivesdk"
    }
}

# /start command
def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton(subject, callback_data=subject)] for subject in file_links]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("📚 Select a subject:", reply_markup=reply_markup)

# Subject button clicked
def subject_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    subject = query.data
    keyboard = [[InlineKeyboardButton(name, callback_data=f"{subject}|{name}")]
                for name in file_links[subject]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=f"📁 {subject} files:", reply_markup=reply_markup)

# File button clicked
def file_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    subject, filename = query.data.split("|")
    link = file_links[subject][filename]
    query.message.reply_text(f"🔗 *{filename}*:\n{link}", parse_mode="Markdown")

# Bot setup
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(subject_handler, pattern="^(Physics|Chemistry)$"))
dp.add_handler(CallbackQueryHandler(file_handler, pattern="^(Physics|Chemistry)\|"))

print("📦 StudyBot is running...")
updater.start_polling()
updater.idle()
