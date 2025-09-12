import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://business.eshop.orange.be/en/mobile/tariff-plans")
time.sleep(3)
driver.maximize_window()
print(driver.title)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
time.sleep(3)
#driver.find_element(By.XPATH, "//a[text() = 'international rates and options']").click()
#driver.find_element(By.LINK_TEXT, "https://business.orange.be/en/mobile/international-and-roaming").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'international text')]").click()

time.sleep(2)
driver.quit()

