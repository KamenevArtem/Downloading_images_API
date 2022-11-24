import requests
import pathlib
import os
from dotenv import load_dotenv
from pathlib import Path
from general_functions import parse_arg_main
from general_functions import define_extension
from general_functions import saving_img


def parse_nasa(access_token, file_dir):
    api_url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": {access_token},
        "start_date": "2022-09-10",
        "end_date": "2022-10-25",
    }
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    pics_data = response.json()
    for pic_number, pic_data in enumerate(pics_data):
        media_type = pic_data["media_type"]
        if media_type == "image":
            nasa_link = pic_data["url"]
            pic_extension = define_extension(nasa_link)
            img_name = f"APOD_{pic_number}.{pic_extension}"
            file_path = Path(file_dir).joinpath(img_name)
            saving_img(nasa_link, file_path)

        
def main():
    load_dotenv()
    access_token = os.environ["NASA_API_KEY"]
    args = parse_arg_main()
    file_dir = args.directory
    script_path = pathlib.Path.cwd()
    file_path = script_path.joinpath(file_dir)
    file_path.mkdir(exist_ok=True)
    parse_nasa(access_token, file_path)
    
    
if __name__ == "__main__":
    main()
