import os
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, '''Добро пожаловать! Я ваш персональный помощник в Telegram и готов ответить на все ваши вопросы и помочь с любыми задачами. Моя цель — сделать ваше взаимодействие максимально простым и продуктивным.

        Как я могу вам помочь?
        Я здесь, чтобы предоставить вам всю необходимую информацию и поддержку. Вы можете выбрать одну из следующих опций:
        
        Часто задаваемые вопросы (FAQ): Здесь вы найдете ответы на самые популярные вопросы, которые помогут быстро разобраться в интересующих вас темах. Это идеальное место для начала, если у вас есть общие вопросы или вам нужна быстрая справка. Чтобы посмотреть часто задаваемые вопросы нажмите /frequent_questions
        
        Помощь и поддержка: Если вам нужна более подробная информация, выберите вариант /support и мы вас переведем к технической помощи.
        Просто ничего: Если вы просто зашли посмотреть или у вас нет срочных вопросов, вы можете выбрать эту опцию и продолжить пользоваться Telegram как обычно. Я всегда буду на связи, когда вам понадобится моя помощь!
''')
@bot.message_handler(commands=['frequent_questions'])
def handle_frequent_questions(message):
    bot.send_message(message.chat.id, '''Вот список часто задаваемых вопросов: Как оформить заказ? Как узнать статус моего заказа? Как отменить заказ? Что делать, если товар пришел поврежденным? Как узнать информацию о доставке? Для того тобы задать вопрос напишите / а потом ваш вопрос. Например: /Как оформить заказ?''')

@bot.message_handler(commands=['/как оформить заказ'])
def handle_support(message):