import telegram
import os
import pathlib
import random
import time
from dotenv import load_dotenv
from general_functions import *


def bot(api_token, script_path, img_quantity, sleep_time, file_dir):
    bot = telegram.Bot(token = api_token)
    files_name = [] 
    for adress, dirs, files in os.walk(f'{script_path}/{file_dir}'):
        for name in files:
            files_name.append(name)
    random.shuffle(files_name)
    quantity = 0
    while True:
        random.shuffle(files_name)
        for file_name in files_name:
            if quantity >= int(img_quantity):
                print("All images have been posted")
                break
            quantity += 1
            time.sleep(int(sleep_time)*3600)
            bot.send_document(chat_id=bot.get_updates()[-1].message.chat_id,
                              document=open(f'{script_path}/{file_dir}/{file_name}', 'rb'))
            print(quantity)


def main():
    load_dotenv()
    args = parse_arg_bot()
    img_quantity = args.img_quantity
    sleep_time = args.sleep_time
    file_dir = args.directory
    script_path = pathlib.Path.cwd()
    access_token = os.environ["telegram_api_key"]
    bot(access_token, script_path, img_quantity, sleep_time, file_dir) 


if __name__ == "__main__":
    args = parse_arg_bot()
    main()
    