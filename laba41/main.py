import telebot
import requests
import json

API = "73d5abf2"

bot = telebot.TeleBot('6775096030:AAEIEoT4yViWJEL371A_RaroQo_VZVOjVoI')

@bot.message_handler(commands=['/start'])
def handle_start(message):
    bot.reply_to(message, f'Hi {message.from_user.first_name} {message.from_user.last_name}! I am a PovMovie_Bot bot, I was created to prompt you in the field of movies! I hope you enjoy it. \n /help - help on commands and bot.')

@bot.message_handler(commands=['/help'])
def handle_help(message):
    bot.reply_to(message, f' List of commands:' "\n" "/start - Greeting and introduction to the bot" "\n""/help - List of commands and assistant" "\n""/top - The best movies of all the time""\n" "Movie name - displays all information about this movie (for a better search, it is better to specify the full name of the movie)" "\n")

@bot.message_handler(commands=['/top'])
def handle_top(message):
    bot.reply_to(message,f' The 10 best movies of all time: ' "\n"  "1.The Green Mile" "\n"  "2.The Shawshank Redemption" "\n"  "3.Forrest Gump" "\n"  "4.The intouchables" "\n"  "5.Schindler's List" "\n"  "6.Interstellar" "\n"  "7.The Lord of the Rings: The Return of the King" "\n"  "8.Fight Club" "\n"  "9.Pulp Fiction" "\n"  "10.Coco" '')

@bot.message_handler()
def info(message):
    if (message.text.lower() == '/help'):
        handle_help(message)
    elif (message.text.lower() == '/start'):
        handle_start(message)
    elif (message.text.lower() == '/top'):
        handle_top(message)
    else:
        MovieName = message.text.lower()
        api_url = f"http://www.omdbapi.com/?t={MovieName}&apikey={API}"
        try:
            response = requests.get(api_url)
            data = json.loads(response.text)
            text = f'<b>Title:</b> {data["Title"]} 🔥 \n<b>Year:</b> {data["Year"]} 🎬 \n<b>Rated:</b> {data["Rated"]} 🔞 \n<b>Runtime:</b> {data["Runtime"]} 🕞 \n<b>Genre:</b> {data["Genre"]} 💫 \n<b>Rating(imdbRating):</b> {data["imdbRating"]} ⭐ \n<b>Rating(Metascore):</b> {data["Metascore"]} ⭐ \n<b>BoxOffice:</b> {data["BoxOffice"]} 💰 \n<b>Released:</b> {data["Released"]} 📅  \n<b>Actors:</b> {data["Actors"]} 💥 \n<b>Director:</b> {data["Director"]} 💯 \n<b>Writer:</b> {data["Writer"]} 💬 \n  \n<b>Plot:</b> {data["Plot"]} \n'
            photo_url = data["Poster"]
            bot.send_message(message.chat.id, text, parse_mode="html")
            bot.send_photo(message.chat.id, photo_url)
        except:
            bot.reply_to(message, "<b>The movie is specified incorrectly ⛔</b>", parse_mode ='html')
bot.polling()
