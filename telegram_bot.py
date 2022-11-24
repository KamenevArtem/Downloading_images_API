import telegram
import os
import pathlib
import random
import time
import argparse
from retry import retry
from pathlib import Path
from dotenv import load_dotenv


def parse_args_bot():
    parser = argparse.ArgumentParser()
    parser.add_argument('-st', '--sleep_time', nargs='?', type=float, help='Publication frequency in hours',
                        default = "1")
    parser.add_argument('-d', '--directory', help='Directory where needed to be post images are located',
                        default='Images')
    arg = parser.parse_args()
    return arg


def get_file_paths(file_path):
    file_paths = [] 
    for adress, file_directory, files in os.walk(file_path):
        for name in files:
            file_paths.append(Path(adress).joinpath(name))
    return(file_paths)


def send_image(bot, file_path, tg_chat_id):
    with open(file_path, 'rb') as posting_file:
        bot.send_document(chat_id=tg_chat_id, 
                        document=posting_file)


@retry((telegram.error.NetworkError, ConnectionError), delay=1, backoff=4, max_delay=4)
def send_images_to_tg_channel(api_token, file_path, sleep_time, tg_chat_id):
    bot = telegram.Bot(token = api_token)
    file_paths = get_file_paths(file_path)
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
    file_path = script_path.joinpath(file_dir)
    access_token = os.environ["TG_API_KEY"]
    chat_id = os.environ["TG_CHAT_ID"]
    send_images_to_tg_channel(access_token, file_path, sleep_time, chat_id)


if __name__ == "__main__":
    main()
