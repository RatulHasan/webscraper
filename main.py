from bs4 import BeautifulSoup
import requests

search = input("Enter search query: ")
params = {"q": search}

r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html5lib")

f = open("soup.html", "w+")
f.write(soup.prettify())

print(soup.prettify())