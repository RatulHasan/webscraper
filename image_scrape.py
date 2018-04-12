from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

search = input("Enter search query: ")
params = {"q": search}

r = requests.get("https://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

links = soup.findAll("a", {"class": "thumb"})

if not os.path.exists("./scraped_images/"+search):
    os.makedirs("./scraped_images/"+search)
    path = "./scraped_images/"+search + "/"
else:
    path = "./scraped_images/"+search + "/"

for item in links:
    img_obj = requests.get(item.attrs["href"])
    img_link = item.attrs["href"]
    title = item.attrs["href"].split("/")[-1]
    try:
        image = Image.open(BytesIO(img_obj.content))
        image.save(path + title, image.format)
        print(title)
    except ImportError as e:
        print (e)


