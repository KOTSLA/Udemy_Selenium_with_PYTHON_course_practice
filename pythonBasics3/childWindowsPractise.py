import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpenedList = driver.window_handles
driver.switch_to.window(windowsOpenedList[1])
childWindowsSelectedText = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text

print(childWindowsSelectedText)

driver.switch_to.window(windowsOpenedList[0])
driver.find_element(By.ID, "username").send_keys(childWindowsSelectedText)
driver.find_element(By.ID, "password").send_keys("learning")

driver.find_element(By.XPATH, "//input[@value='user']").click()

WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='okayBtn']"))).click()

dropdown = Select(WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login-form']/div[5]/select"))))
dropdown.select_by_visible_text("Consultant")

driver.find_element(By.XPATH, "//input[@id='terms']").click()

driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

errorText = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='login-form']/div[1]"))).text

print(errorText)


time.sleep(2)