import os
import urllib.parse
import argparse
from urllib.parse import urlparse
from pathlib import Path


def create_dir(script_path, im_path):
    try:
        Path(f"{script_path}/{im_path}").mkdir(exist_ok=True)
    except FileExistsError:
        pass
    return    


def define_extension(file_url):
    parsed_url = urlparse(file_url)
    resulting_path = parsed_url.path
    resulting_path = urllib.parse.unquote(resulting_path)
    (file_path, file_extension) = os.path.splitext(resulting_path)
    return file_extension


def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--module', nargs='?', help='Enter which module you want to use')
    parser.add_argument('-u', '--url', nargs='?', help='Url for downloading image')
    arg = parser.parse_args()
    return arg    
