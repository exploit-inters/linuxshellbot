import telebot

from subprocess import Popen, PIPE, STDOUT

from conf import *

bot = telebot.TeleBot(TOKEN)

allowedusers = [243687606] #insert your ID

@bot.message_handler(func=lambda message: True)
def executecomands(message):
   if message.from_user.id in allowedusers:
      if message.text.startswith('!exec'):
        command = " ".join(message.text.split(" ", 1)[1:])
        things = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = things.stdout.read()
        bot.send_message(message.chat.id, output)
      return
   return
bot.polling(none_stop=True)
