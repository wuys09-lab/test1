# test_baidu.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    # 启动浏览器
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    yield driver
    driver.quit()


def test_baidu_search(driver):
    # 定位搜索框，输入搜索词
    search_box = driver.find_element(By.ID, "kw")
    search_box.send_keys("自动化测试")

    # 定位搜索按钮，点击
    search_button = driver.find_element(By.ID, "su")
    search_button.click()

    # 等待搜索结果出现
    wait = WebDriverWait(driver, 10)
    result = wait.until(EC.presence_of_element_located((By.ID, "content_left")))

    # 断言搜索结果页面包含“自动化测试”关键词
    assert "自动化测试" in driver.title