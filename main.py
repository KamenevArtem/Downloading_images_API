import requests
import pathlib
import os
import urllib.parse
import datetime
from urllib.parse import urlparse
from dotenv import load_dotenv
from general_functions import *  


def parse_im(url, script_path, im_path):
    create_dir(script_path, im_path)
    image_name = "hubble.jpg"
    response = requests.get(url)
    response.raise_for_status
    with open(f"{script_path}/{im_path}/{image_name}", "wb") as saved_im:
        saved_im.write(response.content)
    return


def fetch_spacex_last_launch(script_path, im_path):
    create_dir(script_path,im_path)
    url_template = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url_template)
    response.raise_for_status
    img_links = response.json()
    for img_number, img_link in enumerate(img_links["links"]["flickr"]["original"]):
        image_request = requests.get(img_link)
        image_request.raise_for_status
        image_name = f"spacex_{img_number}.jpg"
        with open(f"{script_path}/{im_path}/{image_name}", "wb") as saved_img:
            saved_img.write(image_request.content)
    return


def parse_nasa(access_token, script_path, im_path):
    create_dir(script_path, im_path)
    api_url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": {access_token},
        "start_date": "2022-09-10",
        "end_date": "2022-10-25",
    }
    response = requests.get(api_url, params=payload)
    response.raise_for_status
    pics_data = response.json()
    for pic_number, pic_data in enumerate(pics_data):
        nasa_link = pic_data["url"]
        link_condition = urlparse(nasa_link).netloc
        if link_condition == "apod.nasa.gov":
            image_request = requests.get(nasa_link)
            image_request.raise_for_status
            pic_extension = define_extension(nasa_link)
            image_name = f"APOD_{pic_number}{pic_extension}"
            with open(f"{script_path}/{im_path}/{image_name}", "wb") as saved_img:
                saved_img.write(image_request.content)
        else:
            pass


def parse_EPIC(access_token, script_path, im_path):
    create_dir(script_path, im_path)
    api_url = "https://api.nasa.gov/EPIC/api/natural/image"
    url_template = "https://api.nasa.gov/EPIC/archive/natural/{}"
    payload = {
        "api_key": {access_token},
    }
    response = requests.get(api_url, params=payload)
    response.raise_for_status
    res = response.json()
    for pic_number, data in enumerate(res):
        pic_date = data["identifier"]
        mean_index = int(len(pic_date)/2)+1
        pic_date = pic_date[: mean_index]
        pic_date = f"{pic_date[0:4]}-{pic_date[4:6]}-{pic_date[6:8]}"
        pic_date = datetime.date.fromisoformat(pic_date)
        pic_name = data["image"]
        parsed_link = f"{pic_date.year}/{pic_date.month}/{pic_date.day}/png/{pic_name}.png"
        url = url_template.format(parsed_link)
        print(url)
        image_request = requests.get(url, params=payload)
        image_request.raise_for_status
        image_name = f"EPIC_{pic_number}.png"
        with open(f"{script_path}/{im_path}/{image_name}", "wb") as saved_img:
            saved_img.write(image_request.content)        


def main():
    load_dotenv()
    nasa_api_token = os.environ["api_key"]
    script_path = pathlib.Path.cwd()
    url = input("Введите ссылку для скачивания: ")
    im_path = input("Введите название директории, куда необходимо скачать файл: ")
    parse_im(url, script_path, im_path)
    fetch_spacex_last_launch(script_path, im_path)
    parse_EPIC(nasa_api_token, script_path, im_path)
    parse_nasa(nasa_api_token, script_path, im_path)


if __name__ == "__main__":
    main()
