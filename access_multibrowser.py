# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:41:49 2020

@author: aditipc

Description: This code explains how to access Chrome and Firefox Browser and 
performs basic commands of fetching title, URL and HTML code of webpage.
"""

from selenium import webdriver

# Driver to access Firefox Browser
driver = webdriver.Firefox(executable_path="C:\Driver\geckodriver-v0.26.0-win64\geckodriver.exe")

# Driver to access Chrome Browser
# driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.co.in")

print(driver.title) # Return title of the webpage

print(driver.current_url) # Return URL of the webpage

print(driver.page_source) # Return HTML code of the webpage

driver.close() # Close the webdriver