import requests
import pathlib
from dotenv import load_dotenv
from general_functions import parse_arg_main
from general_functions import saving_img


def fetch_spacex_last_launch(script_path, im_path, flight_id):
    url_template = "https://api.spacexdata.com/v5/launches/{}"
    url = url_template.format(flight_id)  
    response = requests.get(url)
    response.raise_for_status()
    img_links = response.json()
    for img_number, img_link in enumerate(img_links["links"]["flickr"]["original"]):
        pic_extension = ".jpg"
        img_name = f"spacex_{img_number}"
        saving_img(pic_extension, img_link, script_path, im_path, img_name)
        

def main():
    script_path = pathlib.Path.cwd()
    load_dotenv()
    args = parse_arg_main()
    im_path = args.directory
    flight_id = args.flight
    fetch_spacex_last_launch(script_path, im_path, flight_id)
    
    
if __name__ == "__main__":
    main()
