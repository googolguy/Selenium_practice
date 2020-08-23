# -*- coding: utf-8 -*-
"""
Description: Working with Links | Operation on Web links | Handling links
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present: ", len(links)) # How many links present in page.

print("Link names in the webpage:-")
for item in links:
    print(item.text)

# To click on a link.
driver.find_element(By.LINK_TEXT, "REGISTER").click()  # Using complete link

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click() # Using partial link

time.sleep(5)

driver.close()