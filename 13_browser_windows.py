# -*- coding: utf-8 -*-
"""
Description: Working with Browser windows.
"""
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="Multiple"]/button').click()

print(driver.current_window_handle)  # Return parent handle values

handles = driver.window_handles  # Return handle values of all opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print("Page Title:", driver.title, ", Handle:", handle)

# To close any specific window
for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == "www.sakinalium.in":
        driver.close()

time.sleep(5)

driver.quit()
