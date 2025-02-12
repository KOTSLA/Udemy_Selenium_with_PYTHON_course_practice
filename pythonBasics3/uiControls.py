import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#radio buttons un checkbox select if it's positions can be changed
# select checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()

# select radio buttons

radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radiobuttons))

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

time.sleep(2)

#radio buttons un checkbox select if it's positions can not be changed
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# element hide/show
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(2)
