from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chromium driver library
driver = ChromeDriverManager().install()
driver = Chrome(service=Service(driver))

# target api
driver.get('https://www.worldometers.info/coronavirus/country/philippines/')
sleep(1)

# extract data
totalDeath = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[5]").text
totalCases = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[4]").text
totalRecov = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[6]").text
miscUpdate = driver.find_element(By.XPATH, "//div[@id='news_block']").text

print(f"Cases: {totalCases}")
print(f"Death: {totalDeath}")
print(f"Recov: {totalRecov}")
print(f"Updat: {miscUpdate}")
print("__________________\n")
