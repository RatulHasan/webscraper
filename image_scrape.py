from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = input("Enter search query: ")
    params = {"q": search}

    r = requests.get("https://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.findAll("a", {"class": "thumb"})

    dir_name = "./scraped_images/" + search.replace(" ", "_").lower()

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            # img_link = item.attrs["href"]
            title = item.attrs["href"].split("/")[-1]
            try:
                image = Image.open(BytesIO(img_obj.content))
                image.save("./" + dir_name + "/" + title, image.format)
                print(title)
            except:
                print("Could not save image")

        except:
            print("Could not requests!")

    StartSearch()

StartSearch()


