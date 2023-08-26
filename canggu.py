from playwright.sync_api import sync_playwright
import time
import pandas as pd


playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
page.goto('https://www.bukitvista.com/bali-vacation-rentals')
time.sleep(3)

for i in range(1, 4):
    print(i)
    page.locator('#fave-pagination-loadmore > a[data-area="canggu"]').click()
    time.sleep(3)

parser = page.inner_html('section[data-id="22f7697"]')

browser.close()
playwright.stop()