import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

def print_hi(name):

    driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
    driver.maximize_window()
    wait = WebDriverWait(driver, 50)
    driver.get('https://www.ynet.co.il/')
    time.sleep(2)
    wait.until(driver.find_element_by_link_text("logo").click())

    search_box = driver.find_element_by_name("topStoryDate")

    print(search_box.tag_name)

    time.sleep(5)

    driver.quit()

if __name__ == '__main__':
    print_hi('PyCharm')
