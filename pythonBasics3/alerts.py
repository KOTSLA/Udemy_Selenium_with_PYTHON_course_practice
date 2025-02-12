import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

name = "Vjačeslavs"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

driver.find_element(By.CSS_SELECTOR, "#name").clear()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()
confirm = driver.switch_to.alert
confirmText = confirm.text
print(confirmText)
assert name in confirmText
confirm.dismiss()



time.sleep(2)
