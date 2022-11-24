import requests
import pathlib
from dotenv import load_dotenv
from pathlib import Path
from general_functions import parse_arg_main
from general_functions import saving_img


def fetch_spacex_last_launch(file_dir, flight_id):
    url_template = "https://api.spacexdata.com/v5/launches/{}"
    url = url_template.format(flight_id)
    response = requests.get(url)
    response.raise_for_status()
    img_links = response.json()
    for img_number, img_link in enumerate(img_links
                                          ["links"]
                                          ["flickr"]
                                          ["original"]):
        img_name = f"spacex_{img_number}.jpg"
        file_path = Path(file_dir).joinpath(img_name)
        saving_img(img_link, file_path, img_name)


def main():
    load_dotenv()
    args = parse_arg_main()
    flight_id = args.flight
    file_dir = args.directory
    script_path = pathlib.Path.cwd()
    file_path = script_path.joinpath(file_dir)
    file_path.mkdir(exist_ok=True)
    fetch_spacex_last_launch(file_path, flight_id)


if __name__ == "__main__":
    main()
