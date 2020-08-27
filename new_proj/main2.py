import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup



chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")



driver = webdriver.Chrome(options=chrome_options)



def run():

    try:
        driver.get('https://www.tcgplayer.com/search/all/product?q=pokemon')

    except:
        driver = webdriver.Chrome(options=chrome_options)
        print("driver initialized")
        driver.get('https://www.tcgplayer.com/search/all/product?q=pokemon')        
    print("Got the results")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    span = str(soup.find_all('span', class_ = 'inventory')[0]) if soup.find_all('span', class_ = 'inventory') else None
    if span == None:
        print('didnt worked :(((')

    else:
        print("Worked")

    print('span is: ',span)
    return span if span else "Not worked"





