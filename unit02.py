import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def widsize_maximize(self):
        self.driver.maximize_window()#最大化

    def test_title(self):
        self.driver.get("https://www.baidu.com")
        self.assertIn("百度", self.driver.title)

    def test_search(self):
        self.driver.get("https://www.baidu.com")
        search_box = self.driver.find_element(By.ID, "kw")
        search_box.send_keys("unittest")
        #self.driver.find_element(By.ID, "su").click()
        # 断言 URL 包含搜索词
        #self.assertIn("wd=unittest", self.driver.current_url)
    def test_click(self):
        self.driver.get("https://www.baidu.com")
        click = self.driver.find_element(By.ID, "chat-textarea").click()
        self.assertIn("wd=unittest", self.driver.current_url)#添加断言验证
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()