import requests
import json

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-1&sortBy=publishedAt&apiKey=25cf9900bf554554857eb3d312d019c7"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")
