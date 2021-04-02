import requests
from bs4 import BeautifulSoup

result = requests.get('http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html')
soup = BeautifulSoup(result.text, 'html.parser')

book_list = list()

for a in soup.find_all("article", class_ = "product_pod"):
    book_name = a.h3.a.get('title')
    book_price = a.find('p',class_ = 'price_color').text[1:]
    availability = a.find('p',class_ = 'instock availability').text.strip()
    dict_obj = {'title':book_name, 'isAvailable':availability, 'price':book_price}
    book_list.append(dict_obj)

print(book_list)