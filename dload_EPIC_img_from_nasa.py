import datetime
import requests
from general_functions import *


def parse_EPIC(access_token, script_path, im_path):
    create_dir(script_path, im_path)
    api_url = "https://api.nasa.gov/EPIC/api/natural/image"
    url_template = "https://api.nasa.gov/EPIC/archive/natural/{}"
    payload = {
        "api_key": {access_token},
    }
    response = requests.get(api_url, params=payload)
    response.raise_for_status
    response = response.json()
    for pic_number, img_data in enumerate(response):
        pic_date = datetime.datetime.fromisoformat(img_data["date"])
        pic_name = img_data["image"]
        if pic_date.month < 10:
            if pic_date.day < 10:
                link_construction = f"{pic_date.year}/0{pic_date.month}/0{pic_date.day}/png/{pic_name}.png"
            else:
                link_construction = f"{pic_date.year}/0{pic_date.month}/{pic_date.day}/png/{pic_name}.png"
        else:
            if pic_date.day < 10:
                link_construction = f"{pic_date.year}/{pic_date.month}/0{pic_date.day}/png/{pic_name}.png"
            else:
                link_construction = f"{pic_date.year}/{pic_date.month}/{pic_date.day}/png/{pic_name}.png"
        url = url_template.format(link_construction)
        print(url)
        image_request = requests.get(url, params=payload)
        image_request.raise_for_status
        image_name = f"EPIC_{pic_number}.png"
        with open(f"{script_path}/{im_path}/{image_name}", "wb") as saved_img:
            saved_img.write(image_request.content)


