# -*- coding: utf-8 -*-
"""
Description: Working with scrolling a webpage based on requirement.
               -> Scroll down a page based on pixel
               -> scroll down a page till element found
               -> scroll to end of the page
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()  # This will maximize window

# Scroll down a page based on pixel
driver.execute_script("window.scrollBy(0,1000)", "")

time.sleep(3)

# scroll down a page till element found
flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
driver.execute_script("arguments[0].scrollIntoView();", flag)

time.sleep(3)

# scroll to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
