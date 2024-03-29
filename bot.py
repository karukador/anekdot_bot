from config import BOT_TOKEN 
from telebot import TeleBot
import random
from anekdot import anekdots

bot = TeleBot(token=BOT_TOKEN)

help_message = """\
Я умею:
/start - выводит приветственное сообщение
/help - узнать, что я умею
/anekdot - вывод случайного анекдота
"""

warning = """
Анекдоты, как и большинство шуток в интернете, могут быть 'черным юмором'.
Заранее извинияюсь за возможное оскорбительное содержание.
"""

podskaska = """
Чтобы узнать, что я умею введи /help"""
@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}!" + warning + podskaska)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, text=help_message + "в боте уже 63 анекдотов!")

def send_random_anekdot(message):
    anekdot = random.choice(anekdots)
    bot.send_message(message.chat.id, text=anekdot)
    bot.send_message(message.chat.id, text="ещё один анекдот? /anekdot")
bot.message_handler(commands=['anekdot'])(send_random_anekdot)

@bot.message_handler(func=lambda m: True)
def unknown_command(message):
 known_commands = ['/start', '/help', '/person', '/news']
 if message.text.split()[0] not in known_commands:
     bot.reply_to(message, "Некорректный ввод. Введите /help для просмотра доступных функций")
     
bot.polling()

#@anekdotik_Robot
