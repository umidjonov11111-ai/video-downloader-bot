import telebot 
import yt_dlp
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.Telebot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start (message):
  bot.reply _to(message, "Gud morning!") 

@bot.message_handler (func=lamba message: True)
def download_video(message):
  url = message.text 
bot.reply_to(message, "Downloading, wait for a while...")

try: 
  ydl_opts = {
    'format': 'best[filesize<50M]',
    'outtmpl': 'video.%(ext)s',

  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    filename = ydl.prepare_filename(info)

with open(filename, 'rb') as video:
  bot.send_video(message.chat.id, video)

os.remove(filename)

except Exception as e:
bot.reply_to(message, "Sorry...")

bot.polling()
