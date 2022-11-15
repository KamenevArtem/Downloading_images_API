import requests
import pathlib
import os
from dotenv import load_dotenv
from general_functions import parse_arg_main
from general_functions import define_extension
from general_functions import saving_img


def parse_nasa(access_token, script_path, im_path):
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
        nasa_link = pic_data["url"]
        nasa_media_type = pic_data["media_type"]
        if nasa_media_type == "image":
            pic_extension = define_extension(nasa_link)
            img_name = f"APOD_{pic_number}"
            req_par = ""
            saving_img(pic_extension, nasa_link, script_path, im_path, img_name, req_par)

        
def main():
    script_path = pathlib.Path.cwd()
    load_dotenv()
    access_token = os.environ["NASA_API_KEY"]
    args = parse_arg_main()
    im_path = args.directory
    parse_nasa(access_token, script_path, im_path)
    
    
if __name__ == "__main__":
    main()
