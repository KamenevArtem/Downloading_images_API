import pathlib
from dotenv import load_dotenv
from general_functions import * 
from dload_img_by_url import * 
from dload_spacex_launch_img import *
from dload_nasa_lauch_img import *
from dload_EPIC_img_from_nasa import *


def main():
    load_dotenv()
    args = parse_arg_main()
    using_module = args.module
    input_url = args.url
    flight_id = args.flight
    nasa_api_token = os.environ["api_key"]
    script_path = pathlib.Path.cwd()
    im_path = input("Введите название директории, куда необходимо скачать файл: ")
    if using_module == "Epic":
        parse_EPIC(nasa_api_token, script_path, im_path)
    if using_module == "Img":
        if input_url is None:
            download_img("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
                         , script_path, im_path)
        else:
            download_img(input_url, script_path, im_path)
    if using_module == "Nasa":
        parse_nasa(nasa_api_token, script_path, im_path)
    if using_module == "Spacex":
        fetch_spacex_last_launch(script_path, im_path, flight_id)
    if using_module is None:
        if input_url is None:
            download_img("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
                         , script_path, im_path)
        else:
            download_img(input_url, script_path, im_path)
        fetch_spacex_last_launch(script_path, im_path, flight_id)
        parse_EPIC(nasa_api_token, script_path, im_path)
        parse_nasa(nasa_api_token, script_path, im_path)


if __name__ == "__main__":
    main()
