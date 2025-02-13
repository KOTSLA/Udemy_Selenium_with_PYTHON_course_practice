import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(5)

shopButton = driver.find_element(By.XPATH, "//a[contains(@href, '/angularpractice/shop')]")
shopButton.click()

#collect all phone names - PhoneNameList
phoneNameList = []
phoneWebElements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for phone in phoneWebElements:
    phoneName = phone.find_element(By.XPATH, "div/h4/a").text
    phoneNameList.append(phoneName)
    if phoneName == "Blackberry":
        itemAddButton = phone.find_element(By.XPATH, "div/button")
        itemAddButton.click()
print(phoneNameList)

checkoutButton = driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']")
print(checkoutButton.text)
checkoutButton.click()

cardCheckoutButton = driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]/button")
cardCheckoutButton.click()

#dinamic dropdown
# select list of all identified values
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
deliveryCountries = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='suggestions']/ul/li/a")))
print(f"{len(deliveryCountries)} countries in delivery list")

# from list find item with our value and click that
for country in deliveryCountries:
    # print(country.text)
    if country.text == "India":
        country.click()
        break

# find selected item with get_attribute
print(driver.find_element(By.XPATH, "//input[@id='country']").get_attribute("value"))
assert driver.find_element(By.XPATH, "//input[@id='country']").get_attribute("value") == "India"

driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

assert driver.find_element(By.XPATH, "//strong[contains(text(), 'Success!')]").text == "Success!"
driver.find_element(By.XPATH, "//a[@class = 'close']").click()


time.sleep(2)