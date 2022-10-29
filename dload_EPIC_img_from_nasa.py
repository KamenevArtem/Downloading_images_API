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