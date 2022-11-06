import telegram
import os
import pathlib
from dotenv import load_dotenv
from general_functions import *


def bot(api_token, script_path):
    bot = telegram.Bot(token = api_token)
    bot_chat_id = bot.get_updates()[-1].message.chat_id
    bot.send_message(text='Hi devman', chat_id=bot_chat_id)
    bot.send_document(chat_id=bot_chat_id, document=open(f'{script_path}/1.png', 'rb'))     


def main():
    load_dotenv()
    access_token = os.environ["telegram_api_key"]
    script_path = pathlib.Path.cwd()
    bot(access_token, script_path) 


if __name__ == "__main__":
    args = parse_arg_bot()
    main()
    