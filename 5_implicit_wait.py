# -*- coding: utf-8 -*-
"""
Description: Used to synchronize between code execution and response of appliction.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/index.php")  # Opening URL might take time

driver.implicitly_wait(10)  # Seconds for wait time.
# This wait statement is applicable for all the elements of the page.
# we have to specify this only once in code.

assert "Welcome: Mercury Tours" in driver.title
# This will check if statement entered is there in title fetched by driver and will return a boolean value

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("submit").click()

driver.close()