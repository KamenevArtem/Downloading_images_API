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


def get_file_paths(path, dir):
    file_paths = [] 
    for adress, dirs, files in os.walk(os.path.join(path, dir)):
        for name in files:
            file_paths.append(os.path.join(adress, name))
    return(file_paths)


def send_image(bot, file_path, tg_chat_id):
    with open(file_path, 'rb') as posting_file:
        bot.send_document(chat_id=tg_chat_id, 
                        document=posting_file)


def sending_images_bot(api_token, script_path, sleep_time, file_dir, tg_chat_id):
    bot = telegram.Bot(token = api_token)
    file_paths = get_file_paths(script_path, file_dir)
    while True:
        random.shuffle(file_paths)
        for file_path in file_paths:
            send_image(bot, file_path, tg_chat_id)
            time.sleep(sleep_time*60)


def main():
    load_dotenv()
    args = parse_args_bot()
    sleep_time = args.sleep_time
    file_dir = args.directory
    script_path = pathlib.Path.cwd()
    access_token = os.environ["TG_API_KEY"]
    chat_id = os.environ["TG_CHAT_ID"]
    sending_images_bot(access_token, script_path, sleep_time, file_dir, chat_id)


if __name__ == "__main__":
    main()
