import requests
from bs4 import BeautifulSoup

data = requests.get("http://books.toscrape.com/").content # request the html page content
soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify()) # prettify add spaces and tabulations to html tags

product_s = '.product_pod h3 a' # end point element tag: <a />
price_s = '.price_color'
star_s = '.star-rating'

rating_mappings = {
    "One":   "★",
    "Two":   "★ ★",
    "Three": "★ ★ ★",
    "Four":  "★ ★ ★ ★",
    "Five":  "★ ★ ★ ★ ★"
}

def get_star(tag):
    for key, value in rating_mappings.items():
        if key in tag['class']:
            return value


products = soup.select(product_s)
prices = soup.select(price_s)
ratings = soup.select(star_s)

for product, price, rating in zip(products, prices, ratings):
    title = product['title']
    price = price.string
    star = get_star(rating)

    with open('files/scrapint-books.txt', 'a', encoding='utf-8') as books_file:
        book = f'{title}: {price} - {star}'
        books_file.write(book + '\n')