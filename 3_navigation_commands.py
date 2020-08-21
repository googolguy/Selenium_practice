# -*- coding: utf-8 -*-
"""
Description: Navigational commands that act as forward and back arrow key of browser.
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")  # Tour page
time.sleep(5)

print(driver.title)

driver.get("http://www.pavantestingtools.com/")  # Testing page
time.sleep(5)

print(driver.title)

driver.back()  # Navigate back to Tour page

print(driver.title)

driver.forward()  # Navigate forward to Testing page
time.sleep(5)

print(driver.title)

driver.close()  # Close the current tab of browser
