import telegram
import os
import pathlib
import random
import time
import argparse
from dotenv import load_dotenv


def parse_args_bot():
    parser = argparse.ArgumentParser()
    parser.add_argument('-st', '--sleep_time', nargs='?', type=float, help='Publication frequency in hours',
                        default = "1")
    parser.add_argument('-d', '--directory', help='Directory where needed to be post images are located',
                        default='Images')
    arg = parser.parse_args()
    return arg


def get_file_names(path, dir):
    file_names = [] 
    for adress, dirs, files in os.walk(os.path.join(path, dir)):
        for name in files:
            file_names.append(name)
    return file_names


def send_images(api_token, script_path, sleep_time, file_dir, tg_chat_id):
    bot = telegram.Bot(token = api_token)
    files_name = get_file_names(script_path, file_dir)
    while True:
        random.shuffle(files_name)
        for file_name in files_name:
            time.sleep(sleep_time*60)
            with open(os.path.join(script_path, file_dir, file_name), 'rb') as posting_file:
                bot.send_document(chat_id=tg_chat_id, 
                                document=posting_file)


def main():
    load_dotenv()
    args = parse_args_bot()
    sleep_time = args.sleep_time
    file_dir = args.directory
    script_path = pathlib.Path.cwd()
    access_token = os.environ["TG_API_KEY"]
    chat_id = os.environ["TG_CHAT_ID"]
    send_images(access_token, script_path, sleep_time, file_dir, chat_id) 


if __name__ == "__main__":
    main()
