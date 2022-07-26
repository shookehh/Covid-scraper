from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# chromium driver library
driver = ChromeDriverManager().install()
driver = Chrome(service=Service(driver))

# https://doh.gov.ph/covid19tracker
# bed occupancy 
# number of facilities
# region/province scope
# equipment availability 
# occupied and vacancies

# target secondhand source
driver.get('https://www.worldometers.info/coronavirus/country/philippines/')
sleep(1)

# extract data
tcases = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[4]").text[19:]
tdeath = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[5]").text[8:]
trecov = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[6]").text[11:]
mupdat = driver.find_element(By.XPATH, "//div[@id='news_block']").text

# updates
ccdate = mupdat[12:19]
ncases = mupdat[34:39]
ndeath = mupdat[54:56]

print(f"Cases: {tcases}") # total cases
print(f"Death: {tdeath}") # total death
print(f"Recov: {trecov}") # total recov
print(f"Curnt: {ccdate}") # latest date  
print(f"Newca: {ncases}") # latest cases
print(f"Newde: {ndeath}") # latest death
print("__________________\n")