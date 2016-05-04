TOKEN = '224119801:AAHVzVGytQUIAcnMCAVNTHksB_hqArzCsvY'
DEST = '9083329'

bot = telebot.TeleBot(TOKEN)

bot.send_message(DEST, 'Fim da prova.')
