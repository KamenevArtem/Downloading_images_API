import requests
from general_functions import create_dir


def download_img(url, script_path, im_path):
    create_dir(script_path, im_path)
    image_name = "hubble.jpg"
    response = requests.get(url)
    response.raise_for_status
    with open(f"{script_path}/{im_path}/{image_name}", "wb") as saved_im:
        saved_im.write(response.content)
    return
