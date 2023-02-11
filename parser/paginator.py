import requests
from config.settings import headers
from bs4 import BeautifulSoup as Bs


class Paginator:
    def __init__(self, url):
        self.url = url

    def _get_html(self):
        request = requests.get(url=self.url, headers=headers)
        return request.text

    def _get_soup(self):
        soup = Bs(self._get_html(), 'lxml')
        return soup

    def find_button_next(self):
        pagination = self._get_soup().find('div', class_='pagination')
        return 'Next' in pagination.text