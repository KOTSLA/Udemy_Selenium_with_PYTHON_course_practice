
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")       #chrome headless mode
#chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)       #add parameter
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

#scroll page to button with java script
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#do a screenshot with Java Script
driver.get_screenshot_as_file("screen.png")

time.sleep(2)