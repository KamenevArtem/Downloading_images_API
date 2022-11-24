import datetime
import requests
import pathlib
import os
from dotenv import load_dotenv
from pathlib import Path
from general_functions import parse_arg_main
from general_functions import saving_img


def parse_epic(access_token, file_dir):
    api_url = "https://api.nasa.gov/EPIC/api/natural/image"
    url_template = "https://api.nasa.gov/EPIC/archive/natural/{}"
    api_param = {
        "api_key": {access_token},
    }
    response = requests.get(api_url, api_param)
    response.raise_for_status()
    response = response.json()
    for pic_number, img_data in enumerate(response):
        pic_date = datetime.datetime.fromisoformat(img_data["date"])
        pic_name = img_data["image"]
        link_construction = f"{pic_date:%Y/%m/%d}/png/{pic_name}.png"
        url = url_template.format(link_construction)
        img_name = f"EPIC_{pic_number}.png"
        file_path = Path(file_dir).joinpath(img_name)
        saving_img(url, file_path, api_param)    


def main():
    load_dotenv()
    access_token = os.environ["NASA_API_KEY"]
    args = parse_arg_main()
    file_dir = args.directory
    script_path = pathlib.Path.cwd()
    file_path = script_path.joinpath(file_dir)
    file_path.mkdir(exist_ok=True)
    parse_epic(access_token, file_path)
    
    
if __name__ == "__main__":
    main()
