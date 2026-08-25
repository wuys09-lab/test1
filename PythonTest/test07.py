'''import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# isDisplayed
is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()'''


import unittest
from selenium import webdriver


class SeleniumTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def test_page_title(self):
        self.driver.get("https://selenium.dev")
        self.assertIn("Selenium", self.driver.title)