# -*- coding: utf-8 -*-
"""
Description: How to upload a file.
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.implicitly_wait(10)

driver.switch_to.frame("frame-one1434677811")

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:\\Users\\aditipc\\Desktop\\test.jpg")
