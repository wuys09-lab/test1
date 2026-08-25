# 文本分析
text = "Python is a powerful programming language"
words = text.split()

# 统计词频
word_lengths = [len(word) for word in words]
long_words = [word for word in words if len(word) > 5]

print(f"平均单词长度: {sum(word_lengths)/len(word_lengths):.2f}")
print(f"长单词: {long_words}")


# 推荐的方式
with open("test.txt", "w+") as file:
    #content = file.read()
    #print(content)
    #content = file.write('halo')
    content=file.read()
    print(content)
    # 文件会在代码块结束后自动关闭

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