import unittest
import time
from selenium import webdriver

"hihihi"
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        open browser web driver
        """
        cls.driver = webdriver.Chrome("/Users/moshe_ogalbo/test/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def open_browser(self):
        """
        open windows login
        """
        self.driver.get('https://www.ynet.co.il')
        print(self.driver.current_url)
        print(self.driver.title)
        login = self.driver.find_element_by_class_name("login_premium")
        login.click()
        self.driver.back()


    """
    #def open_login(self):
    """


    @classmethod
    def tearDownClass(cls):
        """
        clos windows browser
        """
        time.sleep(2)
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()