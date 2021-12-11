import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
result = requests.get(url+'index'+'.html')
soup = BeautifulSoup(result.text, 'html.parser')
category_key_link_value = {}
book_list = []

for a in soup.find_all('ul')[1].find_all('a'): 
    if a.text:
        category_url = a['href']
        category_url = category_url[:len(category_url)-10]
        category_name = a.get_text().strip()
        category_key_link_value[category_name] = category_url

def book_print():
    for itr in book_list:
        print('{:.<35.30}{}'.format(itr['title'],itr['price']))

def recursive_next_page_and_book_append(link):
    page_request = requests.get(link)
    page_soup = BeautifulSoup(page_request.text, 'html.parser')
    for a in page_soup.find_all("article", class_ = "product_pod"):
        book_name = a.h3.a.get('title')
        book_price = a.find('p',class_ = 'price_color').text[1:]
        availability = a.find('p',class_ = 'instock availability').text.strip()
        dict_obj = {'title':book_name, 'isAvailable':availability, 'price':book_price}
        book_list.append(dict_obj)
    if page_soup.find(attrs={'class':'next'}):
        link = link[:len(link)-11]
        link = link + page_soup.find('li',attrs={'class':'next'}).a.get('href')
        recursive_next_page_and_book_append(link)

def book_genre_list(genre,*argv):
    if genre in category_key_link_value:
        page = url + category_key_link_value.get(genre)
        page_request = requests.get(page)
        page_soup = BeautifulSoup(page_request.text, 'html.parser')
        for a in page_soup.find_all("article", class_ = "product_pod"):
            book_name = a.h3.a.get('title')
            book_price = a.find('p',class_ = 'price_color').text[1:]
            availability = a.find('p',class_ = 'instock availability').text.strip()
            dict_obj = {'title':book_name, 'isAvailable':availability, 'price':book_price}
            book_list.append(dict_obj)
        if page_soup.find(attrs={'class':'next'}):
            page = page + page_soup.find('li',attrs={'class':'next'}).a.get('href')
            recursive_next_page_and_book_append(page)
    else:
        print('No such category available!!')

genre = input('Enter genre: ')
genre = genre.capitalize()
book_genre_list(genre)

book_print()