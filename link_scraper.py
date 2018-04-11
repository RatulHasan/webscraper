from bs4 import BeautifulSoup
import requests

search = input("Enter search query: ")
params = {"q": search}

r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

all_item_text = ""
all_item_href = ""

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]


    if item_text and item_href:
        print(item_text)
        print(item_href)
    all_item_text += item_text + "\n" + item_href + "\n"




f = open(str(search)+".html", "w+")
f.write(all_item_text + all_item_href + "\n")
f.close()