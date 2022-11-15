import os
import urllib.parse
import argparse
import requests
from urllib.parse import urlparse
from pathlib import Path


def create_dir(script_path, im_path):
    Path(os.path.join(script_path, im_path)).mkdir(exist_ok=True) 


def define_extension(file_url):
    parsed_url = urlparse(file_url)
    resulting_path = parsed_url.path
    resulting_path = urllib.parse.unquote(resulting_path)
    file_path, file_extension = os.path.splitext(resulting_path)
    return file_extension


def parse_arg_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--flight', nargs='?', help='Flight id for Nasa launch',
                        default="5eb87d47ffd86e000604b38a")
    parser.add_argument('-d','--directory', nargs='?', help='Directory where images should be downloaded',
                        default = 'Images')
    arg = parser.parse_args()
    return arg


def saving_img(pic_extension, link, script_path, im_path, pic_name, req_par):
    create_dir(script_path, im_path)
    image_request = requests.get(link, params = req_par)
    image_request.raise_for_status()
    image_name = f"{pic_name}{pic_extension}"
    with open(os.path.join(script_path, im_path, image_name), "wb") as saved_img:
        saved_img.write(image_request.content)

