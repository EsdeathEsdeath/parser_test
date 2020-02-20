import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):  # return num of pages
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'], data['price'], data['address'], data['url']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item_table')
    for ad in ads:
        # title, item-address, item-date, price, url
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''

        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''

        try:
            address = ad.find('div', class_='data').find('div', class_='item-address').text.strip()
        except:
            address = ''

        data = {'title': title, 'price': price, 'address': address, 'url': url}
        write_csv(data)


def main():
    url = 'https://www.avito.ru/moskva/audio_i_video/muzykalnye_tsentry_magnitoly?q=проигрыватель+винила&p=1'
    base_url = 'https://www.avito.ru/moskva/audio_i_video/muzykalnye_tsentry_magnitoly?'
    page_part = 'p='
    query_part = 'q=проигрыватель+винила&'
    total_pages = get_total_pages(get_html(url))
    for i in range(1, 3):
        url_gen = base_url + query_part + page_part + str(i)
        # print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()
