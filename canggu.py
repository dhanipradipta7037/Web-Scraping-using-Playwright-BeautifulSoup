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

#procces pagination in web
for i in range(1, 4):
    print(i)
    page.locator('#fave-pagination-loadmore > a[data-area="canggu"]').click()
    time.sleep(3)

#procces scraping url
time.sleep(3)
data_villa = []
parser = page.inner_html('section[data-id="22f7697"]')
soup = BeautifulSoup(parser, 'html.parser')
urls = soup.find_all('div', {'class':'item-body flex-grow-1'})
for url in urls:
    time.sleep(2)
    links = url.find('a').get('href')
    list_urls = {'url':links}
    data_villa.append(list_urls)
print(len(data_villa))

#procces save data in csv
df = pd.DataFrame(data_villa)
df.to_csv('canggu_url.csv', index=False)


browser.close()
playwright.stop()