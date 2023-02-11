from fake_useragent import UserAgent
from peewee import PostgresqlDatabase
from selenium import webdriver

options = webdriver.ChromeOptions()
ua = UserAgent()
options.add_argument('--headless')
options.add_argument('--disable-blink-features=AutomationControlled')


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/109.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,de;q=0.7,ar;q=0.6',
}

db = PostgresqlDatabase(
    database='parser',
    user='hello',
    password=1,
    host='localhost',
    port=5432
)