import requests
from general_functions import *


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