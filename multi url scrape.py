from logging import root
from ssl import Options
from tokenize import Double
from unicodedata import digit
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

root = r"C:\Users\User\Downloads\chromedriver_win32\chromedriver.exe"
settings = webdriver.ChromeOptions()
settings.add_argument('headless')
driver = webdriver.Chrome(root, chrome_options=settings)

weeklyweb = "https://www.worldometers.info/coronavirus/weekly-trends/#weekly_table"
mainweb = "https://www.worldometers.info/coronavirus/#main_table"

def weeklycase():
    driver.get(weeklyweb)
    weekly = driver.find_element(By.XPATH, "//tr[41]//td[5]").text
    print("Weekly Case Change %: " + weekly)

def maincase():
    driver.get(mainweb)
    main = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(10) div.row:nth-child(3) div.col-md-8 div.tab-content:nth-child(10) div.tab-pane.active:nth-child(1) div.main_table_countries_div table.table.table-bordered.table-hover.main_table_countries.dataTable.no-footer tbody:nth-child(2) tr.odd:nth-child(45) > td:nth-child(9)").text
    print("Active Cases: " + main)

weeklycase()
sleep(1)
maincase()

