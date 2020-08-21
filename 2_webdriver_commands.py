# -*- coding: utf-8 -*-
"""
Description: Basic webdriver commands
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

# To open a webpage
driver.get("http://demo.automationtesting.in/Windows.html")

# To get the title of the page
print(driver.title)

# To get the URL of the webpage
print(driver.current_url)

# To click a button by selection it using xpath
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# To pause the execution for some time(sec)
time.sleep(5)

# To close the driver(Parent Browser tab)
driver.close()
'''The button clicked will open a new tab in Browser
but the close command will only close the parent tab'''

# To close all the Browser tabs
driver.quit()