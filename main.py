import time
from smtpd import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
driver.maximize_window()


def print_hi(name):

    driver.implicitly_wait(1)
    driver.get('https://www.ynet.co.il/')

    print(driver.current_url)
    print(driver.title)
    time.sleep(5)

    #wait = WebDriverWait(driver, 50)

    #wait.until(driver.find_element_by_class_name("slick-track").aria_role)
    search_box = driver.find_elements_by_class_name("textDiv").\
        find_elements_by_class_name("topStoryDate").text
    driver.refresh()
    print(search_box)
    driver.close()


if __name__ == '__main__':
    print_hi('name')
