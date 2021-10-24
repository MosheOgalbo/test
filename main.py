import time
from selenium import webdriver
import unittest

def print_hi(name):
    driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
    driver.maximize_window()
    driver.get('https://www.ynet.co.il/')

    time.sleep(5)

    search_box = driver.find_elements_by_class_name("textDiv").find_element_by_tag_name("topStoryDate")

    print(search_box)



    time.sleep(5)

    driver.quit()

if __name__ == '__main__':
    print_hi('name')
