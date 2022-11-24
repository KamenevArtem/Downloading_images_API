import os
import urllib.parse
import argparse
import requests
from urllib.parse import urlparse


def define_extension(file_url):
    parsed_url = urlparse(file_url)
    parsed_path = parsed_url.path
    parsed_path = urllib.parse.unquote(parsed_path)
    file_path, file_extension = os.path.splitext(parsed_path)
    return file_extension


def parse_arg_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--flight', nargs='?',
                        help='Flight id for Nasa launch',
                        default="5eb87d47ffd86e000604b38a")
    parser.add_argument('-d', '--directory', nargs='?',
                        help='Directory where images should be downloaded',
                        default='Images')
    arg = parser.parse_args()
    return arg


def saving_img(link, im_path, params=None):
    response = requests.get(link, params)
    response.raise_for_status()
    with open(im_path, "wb") as saved_img:
        saved_img.write(response.content)
