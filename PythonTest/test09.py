'''from androguard.core.resources.public import element
from matplotlib.pyplot import title
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
'''driver.get("https://baidu.com")
'''assert driver.title=='百度一下
print(title)'''
element=driver.find_element(By.XPATH, '//*[@id="chat-textarea"]')
element.clear()
element.send_keys("selenium")
element==driver.find_element(By.XPATH, '//*[@id="chat-submit-button"]')
element.click()'''