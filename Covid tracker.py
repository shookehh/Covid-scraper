
from gettext import gettext
from ssl import Options
from tokenize import Double
from unicodedata import digit
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import html5lib

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
target = 'https://coronavirus.jhu.edu/region/philippines'
driver.get(target)
sleep(1)

# WTF YOU WANT TO DO WITH THAT TARGET URL

cases = driver.find_element(By.XPATH, "//div[@class='RegionOverview_countryOverview__WPnpe']//div//div[@class='ColumnLayout_container__1whCL']")

print(cases.text)
