import time
from smtpd import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()


def print_hi(name):


    driver.get('https://www.ynet.co.il/')

    print(driver.current_url)
    print(driver.title)
    time.sleep(2)
    search_box = driver.find_element_by_class_name("topStoryDate").text
    driver.refresh()



    print(search_box)
    driver.close()


if __name__ == '__main__':
    print_hi('name')
