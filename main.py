import telebot
import subprocess
from conf import *

bot = telebot.TeleBot(TOKEN)

allowedusers = [243687606, 250552323] #insert your ID

@bot.message_handler(func=lambda message: True)
def executecomands(message):
   if message.from_user.id in allowedusers:
      if message.text.startswith('!exec'):
        command = " ".join(message.text.split(" ", 1)[1:])
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        bot.send_message(message.chat.id, str(output.stdout))
      return
   return
bot.polling(none_stop=True)

