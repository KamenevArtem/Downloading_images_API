import datetime
import requests
import pathlib
import os
from dotenv import load_dotenv
from general_functions import parse_arg_main
from general_functions import saving_img


def parse_epic(access_token, script_path, im_path):
    api_url = "https://api.nasa.gov/EPIC/api/natural/image"
    url_template = "https://api.nasa.gov/EPIC/archive/natural/{}"
    payload = {
        "api_key": {access_token},
    }
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    response = response.json()
    for pic_number, img_data in enumerate(response):
        pic_date = datetime.datetime.fromisoformat(img_data["date"])
        pic_name = img_data["image"]
        link_construction = f"{pic_date.year}/{pic_date.month}/{pic_date.day}/png/{pic_name}.png"
        url = url_template.format(link_construction)
        pic_extension = ".png"
        img_name = f"EPIC_{pic_number}"
        req_par = payload
        saving_img(pic_extension, url, script_path, im_path, img_name, req_par)    


def main():
    script_path = pathlib.Path.cwd()
    load_dotenv()
    access_token = os.environ["NASA_API_KEY"]
    args = parse_arg_main()
    im_path = args.directory
    parse_epic(access_token, script_path, im_path)
    
    
if __name__ == "__main__":
    main()
