import requests
import pathlib
import os
import urllib.parse
import datetime
from urllib.parse import urlparse
from dotenv import load_dotenv
from general_functions import * 
from dload_img_by_url import * 
from dload_spacex_launch_img import *
from dload_nasa_lauch_img import *
from dload_EPIC_img_from_nasa import *    


def main():
    load_dotenv()
    nasa_api_token = os.environ["api_key"]
    script_path = pathlib.Path.cwd()
    url = input("Введите ссылку для скачивания: ")
    im_path = input("Введите название директории, куда необходимо скачать файл: ")
    download_img(url, script_path, im_path)
    fetch_spacex_last_launch(script_path, im_path)
    parse_EPIC(nasa_api_token, script_path, im_path)
    parse_nasa(nasa_api_token, script_path, im_path)


if __name__ == "__main__":
    main()
