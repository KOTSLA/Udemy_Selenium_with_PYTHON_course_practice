import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)

svg_popup = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))  # Adjust the selector for your SVG

close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']")))

close_button.click()


time.sleep(2)