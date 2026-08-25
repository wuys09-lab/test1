import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        driver.get("http://www.python.org")

        # 验证标题
        self.assertIn("Python", driver.title)

        # 等待搜索框加载并定位
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # 搜索 pycon
        search_box.send_keys("pycon")
        search_box.send_keys(Keys.RETURN)

        # 等待结果加载
        wait.until(EC.presence_of_element_located((By.ID, "content")))

        # 断言无“无结果”提示
        self.assertNotIn("No matching results found.", driver.page_source)

    def tearDown(self):
        self.driver.quit()  # 推荐 quit() 而非 close()

if __name__ == "__main__":
    unittest.main()