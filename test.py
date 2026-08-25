import webbrowser

from selenium.webdriver.chromium import webdriver


def print_hi(name):
    print(f'Hello, {name}')
driver = webdriver.Chrome()
driver.get("https://baidui.com")
driver.maximize_window()
