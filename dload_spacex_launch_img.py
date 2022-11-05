import requests
from general_functions import create_dir


def fetch_spacex_last_launch(script_path, im_path):
    create_dir(script_path,im_path)
    url_template = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url_template)
    response.raise_for_status
    img_links = response.json()
    for img_number, img_link in enumerate(img_links["links"]["flickr"]["original"]):
        image_request = requests.get(img_link)
        image_request.raise_for_status
        image_name = f"spacex_{img_number}.jpg"
        with open(f"{script_path}/{im_path}/{image_name}", "wb") as saved_img:
            saved_img.write(image_request.content)
    return
