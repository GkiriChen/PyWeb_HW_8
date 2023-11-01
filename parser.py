import re
import requests
from bs4 import BeautifulSoup
import json

url_b = 'https://quotes.toscrape.com/'
url = url_b
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


quotes = []
authors = []

while True:
    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = quote.find("div", class_="tags").text.split('\n')[3:-1]

        existing_author_names = [author["fullname"] for author in authors]
        if author not in existing_author_names:
            ref_description = quote.find("a").get("href")
            response = requests.get(url_b + ref_description + '/')
            soup_a = BeautifulSoup(response.text, 'html.parser')

            fullname = soup_a.find("h3", class_="author-title").text
            born_date = soup_a.find("span", class_="author-born-date").text
            born_location = soup_a.find(
                "span", class_="author-born-location").text
            description = soup_a.find("div", class_="author-description").text

            authors.append({"fullname": fullname,
                            "born_date": born_date,
                            "born_location": born_location,
                            "description": re.sub('[\t\r\n]', '', description).strip().replace('/', r'\/')
                            })

        quotes.append({"tags": tags,
                       "quote":  text,
                       "author": author})

    next_button = soup.find("li", class_="next")
    if next_button:
        next_page = next_button.find("a")["href"]
        url = f"http://quotes.toscrape.com{next_page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        break

with open('quotes.json', 'w', encoding='utf-8') as fd:
    json.dump(quotes, fd, ensure_ascii=False, indent=2)

with open("authors.json", "w", encoding='utf-8') as authors_file:
    json.dump(authors, authors_file, ensure_ascii=False, indent=2)