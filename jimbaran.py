from playwright.sync_api import sync_playwright
import time
import pandas as pd
from bs4 import BeautifulSoup

#procces launch playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch()
page = browser.new_page(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
page.goto('https://www.bukitvista.com/bali-vacation-rentals')
page.wait_for_selector('main#main-wrap')
time.sleep(4)

browser.close()
playwright.stop()