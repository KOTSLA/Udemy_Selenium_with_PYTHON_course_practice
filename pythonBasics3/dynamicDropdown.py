import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.maximize_window()

#dinamic dropdown
# select list of all identified values
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

# from list find item with our value and click that
for country in countries:
    # print(country.text)
    if country.text == "India":
        country.click()
        break

# find selected item with get_attribute
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

time.sleep(2)