# -*- coding: utf-8 -*-
"""
Description: Working with alerts.
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)
driver.switch_to.alert.accept()  # Closes alert window using OK button.

time.sleep(3)

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)
driver.switch_to.alert.dismiss()  # Closes alert window using Cancel button.

driver.quit()
