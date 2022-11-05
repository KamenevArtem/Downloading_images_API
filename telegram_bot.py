import telegram
import os
from dotenv import load_dotenv


def bot(api_token):
    bot = telegram.Bot(token = api_token)
    bot_chat_id = bot.get_updates()[-1].message.chat_id
    bot.send_message(text='Hi devman', chat_id=bot_chat_id)
    #bot.send_document(chat_id=bot_chat_id, document=)


def main():
    load_dotenv()
    access_token = os.environ["telegram_api_key"]
    bot(access_token) 


if __name__ == "__main__":
    main()