import sys

TOKEN = '224119801:AAHVzVGytQUIAcnMCAVNTHksB_hqArzCsvY'
DEST = '9083329'

nome_do_candidato = sys.argv[1]

bot = telebot.TeleBot(TOKEN)

bot.send_message(DEST, 'Fim da prova do candidato ' + nome_do_candidato)
