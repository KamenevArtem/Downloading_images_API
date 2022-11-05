import telegram
import os
from dotenv import load_dotenv


def bot(api_token, bot_chat_id):
    bot = telegram.Bot(token = api_token)
    bot.send_message(text='Hi devman', chat_id=bot_chat_id)


def main():
    load_dotenv()
    access_token = os.environ["telegram_api_key"]
    bot_chat_id = os.environ["bot_chat_id"]
    bot(access_token, bot_chat_id) 


if __name__ == "__main__":
    main()