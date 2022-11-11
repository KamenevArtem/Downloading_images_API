import datetime
import requests
from general_functions import saving_img


def parse_EPIC(access_token, script_path, im_path):
    api_url = "https://api.nasa.gov/EPIC/api/natural/image"
    url_template = "https://api.nasa.gov/EPIC/archive/natural/{}"
    payload = {
        "api_key": {access_token},
    }
    try:
        response = requests.get(api_url, params=payload)
        response.raise_for_status()
        response = response.json()
        for pic_number, img_data in enumerate(response):
            pic_date = datetime.datetime.fromisoformat(img_data["date"])
            day = pic_date.strftime("%d")
            month = pic_date.strftime("%m")
            year = pic_date.strftime("%Y")
            pic_name = img_data["image"]
            link_construction = f"{year}/{month}/{day}/png/{pic_name}.png"
            url = url_template.format(link_construction)
            pic_extention = ".png"
            img_name = f"EPIC_{pic_number}"
            req_par = payload
            saving_img(pic_extention, url, script_path, im_path, img_name, req_par)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
