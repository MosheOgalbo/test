import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest

def print_hi(name):

    driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
    driver.maximize_window()
    time.sleep(1)

#    driver.implicitly_wait(5)
    driver.get('https://www.ynet.co.il/')
    print(driver.current_url)
    driver.find_element()
    driver.find_element
    #   wait = WebDriverWait(driver, 20)
    #wait.until(driver.find_element_by_id("main_header_weather").size())
   # search_box = driver.find_element_by_name("topStoryDate").text


   # print(search_box)
    driver.close()
if __name__ == '__main__':
    print_hi('name')
