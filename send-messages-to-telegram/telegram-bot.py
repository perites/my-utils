import telebot

telegram_bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, threaded=False)

telegram_bot.send_message(chat_id=CHAT_ID,text="😈")
