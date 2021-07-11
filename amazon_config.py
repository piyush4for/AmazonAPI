from selenium import webdriver
import sys

DIRECTORY = 'reports'

print("Enter product name: ")
NAME = input()

CURRENCY = '₹'
#if used "," in price then it would make wrong filter url so dont put , in url
MIN_PRICE = ''
print("Enter maximum affordable rate i.e, max price")
MAX_PRICE = input()
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "https://www.amazon.in/"

def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver',chrome_options=options)

#used one line function instead just one line becoz its a good prcatice
def get_web_driver_options():
    return webdriver.ChromeOptions()

#i got from stackoverflow thats the best way to run Selenium
def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')