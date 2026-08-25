import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_title(self):
        self.driver.get("https://www.baidu.com")
        self.assertIn("百度", self.driver.title)

    def test_search(self):
        self.driver.get("https://www.baidu.com")
        search_box = self.driver.find_element(By.ID, "kw")  #id attribute is not available for this element
        search_box.send_keys("unittest")
        self.driver.find_element(By.ID, "su").click()
        # 断言 URL 包含搜索词
        self.assertIn("wd=unittest", self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()