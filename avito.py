import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html): # return num of pages
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def main():
    # https://www.avito.ru/moskva/audio_i_video/muzykalnye_tsentry_magnitoly?q=проигрыватель+винила&p=1
    base_url = 


if __name__ == '__main__':
        main()