import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def print_hi(name):

    driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get('https://www.ynet.co.il/')
    driver.refresh()
    print(driver.current_url)
    print(driver.title)

    wait = WebDriverWait(driver, 20, poll_frequency=2)
    wait.until(driver.find_element_by_class_name("topStoryDate").is_displayed())
    search_box = driver.find_elements_by_class_name("topStoryDate").text
    print(search_box)
    driver.close()
if __name__ == '__main__':
    print_hi('name')
