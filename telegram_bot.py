import telegram
import os
import pathlib
import random
import time
from dotenv import load_dotenv
from general_functions import parse_arg_bot


def get_file_names(path, dir):
    file_names = [] 
    for adress, dirs, files in os.walk(os.path.join(path, dir)):
        for name in files:
            file_names.append(name)
    return file_names


def send_images(api_token, script_path, sleep_time, file_dir):
    bot = telegram.Bot(token = api_token)
    files_name = get_file_names(script_path, file_dir)
    while True:
        random.shuffle(files_name)
        for file_name in files_name:
            time.sleep(int(sleep_time))
            with open(os.path.join(script_path, file_dir, file_name), 'rb') as posting_file:
                bot.send_document(chat_id=bot.get_updates()[-1].message.chat_id, 
                                document=posting_file)


def main():
    load_dotenv()
    args = parse_arg_bot()
    sleep_time = args.sleep_time
    file_dir = args.directory
    script_path = pathlib.Path.cwd()
    access_token = os.environ["TG_API_KEY"]
    send_images(access_token, script_path, sleep_time, file_dir) 


if __name__ == "__main__":
    args = parse_arg_bot()
    main()
