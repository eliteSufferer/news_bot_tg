import telebot
from telebot import types
import utils

bot = telebot.TeleBot('1454525088:AAEhkNU7uPPkFqxk37zjcvDjiAteIWJr09U')

import feedparser


def feed_parser():
    NewsFeed = {"Andro news": 'https://andro-news.com/files/news/news_rss_ru.xml',
                'Amic': 'https://www.amic.ru/rss/',
                'VC': 'https://vc.ru/feed',
                "XDA-Developers": 'https://www.xda-developers.com/feed/',
                "AC/DC": 'http://www.youtube.com/feeds/videos.xml?channel_id=UCB0JSO6d5ysH2Mmqz5I9rIw',
                'Hi-Tech Mail.ru': 'https://hi-tech.mail.ru/rss/all/'}
    message = dict()
    for key in NewsFeed.keys():
        current_news = feedparser.parse(NewsFeed[key]).entries[0]
        message[key] = current_news.title + '\n' + current_news.link
    return message


@bot.message_handler(commands=['start'])
def start_menu(message):
    message_text = 'Здравствуйте!\n' \
                    + 'Наберите /help - для отображения списка доступных команд.'
    bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['help'])
def print_menu(message):
    message_text = 'Вот, что умеет этот бот:\n' \
                    + '/help - отображает список доступных команд\n' \
                    + '/read_rss - присылает сводную информацию из выбранных источников'
    bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['read_rss'])
def read_rss(message):
    post = feed_parser()
    bot.send_message(message.chat.id, 'Новая информация на выбранных площадках:')
    for key in post.keys():
        bot.send_message(message.chat.id, key + '\n' + post[key])


if __name__ == '__main__':
    bot.infinity_polling()
