from selenium import webdriver

driver=webdriver.Chrome()
'''driver.get("https://www.baidu.com")
title =driver.title
print(title)
assert title=='百度'
driver.implicitly_wait(0.5)
driver.close()'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = Options()
# 使用你本机的 Chrome 用户数据目录（会继承你的代理、登录态、证书）
options.add_argument("--user-data-dir=" + os.path.expanduser("~/Library/Application Support/Google/Chrome"))
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://www.baidu.com")
print("✅ 页面标题:", driver.title)
driver.quit()