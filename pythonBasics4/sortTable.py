import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

dropdown = Select(driver.find_element(By.XPATH, "//select[@id='page-menu']"))
dropdown.select_by_visible_text("20")

# click on colum header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all veggie names - BrowserSortedVeggieList
browserSortedVeggies = []
veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElement:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#sort this BrowserSortedVeggieList - newSortedList
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList


time.sleep(2)