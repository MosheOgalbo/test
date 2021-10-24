import time
from selenium import webdriver


def print_hi(name):

    driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get('https://www.ynet.co.il/')
    driver.refresh()
    print(driver.current_url)
    print(driver.title)

    #   wait = WebDriverWait(driver, 20)
    #wait.until(driver.find_element_by_id("main_header_weather").size())
   # search_box = driver.find_element_by_name("topStoryDate").text


   # print(search_box)
    driver.close()
if __name__ == '__main__':
    print_hi('name')
