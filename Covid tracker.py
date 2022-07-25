
from ssl import Options
from tokenize import Double
from unicodedata import digit
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# YOU NEED TO HAVE AN INTERNET CONNECTION FOR THIS TO WORK (obviously)
# MADE BY YA BOI LJ
# BASICALLY BEAUTIFULSOUP.. BUT BETTER.

# CHROME DRIVER IN WHICH SELENIUM CAN USE
# PLEASE CHANGE CHROME DRIVER LOCATION IF ITS IN A DIFFERENT FOLDER !!
chrome_driver = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"
settings = webdriver.ChromeOptions()
settings.add_argument('headless')
driver = webdriver.Chrome(chrome_driver, chrome_options=settings)


# YOUR TARGET URL
target = 'https://www.worldometers.info/coronavirus/country/philippines/'
driver.get(target)
sleep(1)

# WTF YOU WANT TO DO WITH THAT TARGET URL

casestotal = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[4]")
casestotdeath = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[5]")
casesrec = driver.find_element(By.XPATH, "//div[@class='content-inner']//div[6]")
updates = driver.find_element(By.XPATH, "//div[@id='news_block']")

print(casestotal.text)
print(casestotdeath.text)
print(casesrec.text)
print(updates.text)
