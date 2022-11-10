import pathlib
import os
from dotenv import load_dotenv
from general_functions import parse_arg_main
from dload_spacex_launch_img import fetch_spacex_last_launch
from dload_nasa_img import parse_nasa
from dload_EPIC_img_from_nasa import parse_EPIC


def main():
    load_dotenv()
    args = parse_arg_main()
    using_module = args.module
    flight_id = args.flight
    im_path = args.directory
    nasa_api_token = os.environ["NASA_API_KEY"]
    script_path = pathlib.Path.cwd()
    if using_module == "Epic":
        parse_EPIC(nasa_api_token, script_path, im_path)
    if using_module == "Nasa":
        parse_nasa(nasa_api_token, script_path, im_path)
    if using_module == "Spacex":
        fetch_spacex_last_launch(script_path, im_path, flight_id)
    if using_module is None:
        fetch_spacex_last_launch(script_path, im_path, flight_id)
        parse_EPIC(nasa_api_token, script_path, im_path)
        parse_nasa(nasa_api_token, script_path, im_path)


if __name__ == "__main__":
    main()
