import requests
from general_functions import define_extension
from general_functions import saving_img


def parse_nasa(access_token, script_path, im_path):
    api_url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": {access_token},
        "start_date": "2022-09-10",
        "end_date": "2022-10-25",
    }
    try:
        response = requests.get(api_url, params=payload)
        response.raise_for_status
        pics_data = response.json()
        for pic_number, pic_data in enumerate(pics_data):
            nasa_link = pic_data["url"]
            nasa_media_type = pic_data["media_type"]
            if nasa_media_type == "image":
                pic_extention = define_extension(nasa_link)
                img_name = f"APOD_{pic_number}"
                req_par = ""
                saving_img(pic_extention, nasa_link, script_path, im_path, img_name, req_par)
            else:
                pass
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
