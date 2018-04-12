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
i = 0
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    item_desc = item.find("a").parent.parent.find("p").text


    if item_text and item_href:
        print(item_text)
        print(item_href)
        print(item_desc)
        if i == 0:
            all_item_text += "[\n"

        all_item_text += '{ "Title": "'+ item_text + '", \n  "Link": "' + item_href + '",\n  "Desc": "' + item_desc + '"},\n'



    i += 1

all_item_text += "\n]"


f = open(str(search)+".json", "w+")
f.write(all_item_text + all_item_href + "\n")
f.close()