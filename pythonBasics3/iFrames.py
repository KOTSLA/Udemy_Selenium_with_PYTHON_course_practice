
import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame("courses-iframe")         #best to use iframe ID name
iFrameButtonJoinNow = driver.find_element(By.XPATH, "//a[@class = 'btn btn-theme btn-sm btn-min-block']")
iFrameButtonJoinNow.click()


hover_element = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='sub-frame-error']")))
ActionChains(driver).move_to_element(hover_element).perform()
iFrameErrorText = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='sub-frame-error-details']"))).text
print(iFrameErrorText)

driver.switch_to.default_content()   #switch back from iFrame
print(driver.find_element(By.CSS_SELECTOR, "h1").text)


time.sleep(2)