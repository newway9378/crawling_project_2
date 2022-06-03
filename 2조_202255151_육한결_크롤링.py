import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

set_chrome_driver()

driver = webdriver.Chrome(service=Service("/Users/hangyul/PycharmProjects/학교/chromedriver"))
url = 'https://m.kinolights.com/'
driver.get(url)

time.sleep(2)

search = driver.find_element(By.XPATH, '//*[@id="mainNavigation"]/nav/a[2]')
search.click()

time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)
search = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div/section[2]/ul/li[5]/a')
search.click()

time.sleep(2)
search = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[1]/a')
search.click()

movie_list = []
for _ in range(1, 7):
    time.sleep(1)
    driver.execute_script(f"window.scrollTo(0, {_*2.7*100})")

    if _ < 7:
        for i in range(_*4-3,_*4+1):
            try:
                time.sleep(2)
                search = driver.find_element(By.XPATH, f'//*[@id="listArea"]/div[2]/div[{i}]/a')
                search.click()
                time.sleep(2)
            except:
                pass

            try:
                name = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[5]/div[1]/h3').text
                print(f'---{name}---')
            except:
                name = "NAN"
                pass

            try:
                rating = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[5]/div[1]/div/div/div[1]/div').text
                print(f'---{rating}---')
            except:
                rating = "NAN"
                pass

            try:
                date = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[5]/div[1]/p/span[2]').text
                print(f'---{date}년---')
            except:
                date = "NAN"
                pass

            if name != "NAN":
                movie_list.append((name, rating, date))
                driver.back()

            else:
                pass

    else:
        break


print(movie_list)
driver.quit()
