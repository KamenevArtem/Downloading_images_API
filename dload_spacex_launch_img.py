import requests
from general_functions import saving_img


def fetch_spacex_last_launch(script_path, im_path, flight_id):
    url_template = "https://api.spacexdata.com/v5/launches/{}"
    url = url_template.format(flight_id)  
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_links = response.json()
        for img_number, img_link in enumerate(img_links["links"]["flickr"]["original"]):
            pic_extention = ".jpg"
            img_name = f"spacex_{img_number}"
            req_par = ""
            saving_img(pic_extention, img_link, script_path, im_path, img_name, req_par)
        return
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
