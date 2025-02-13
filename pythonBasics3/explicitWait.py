import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

expectedProduktList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
productNameList = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
for productName in productNameList:
    actualList.append(productName.text)
print(actualList)
assert expectedProduktList == actualList


results = driver.find_elements(By.XPATH, "//div[@class='products']/div")    #parent element
count = len(results)
print(count)
assert count == 3
for result in results:
    result.find_element(By.XPATH, "div/button").click()  #child element

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p")
print(len(prices))
total = 0
for price in prices:
    total += float(price.text)
print(total)
assert total == float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
codeText = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(codeText)
assert codeText == "Code applied ..!"

assert total > float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

time.sleep(2)
