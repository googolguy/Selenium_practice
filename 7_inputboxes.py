# -*- coding: utf-8 -*-
"""
Description: Working with input boxes.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

driver.maximize_window()

# To find out number of input boxes in webpage
inputboxes = driver.find_elements(By.CLASS_NAME, 'form-control')
print("Number of input boxes:", len(inputboxes))

# To provide values into Textboxes
driver.find_element_by_name("first_name").send_keys("Piyush")
driver.find_element_by_name("last_name").send_keys("Yadav")
driver.find_element(By.NAME, 'email').send_keys("happy@life.com")

# To get the status of input box
city_box_disp = driver.find_element(By.NAME, 'city').is_displayed()
print("City Box displayed:", city_box_disp)

city_box_ena = driver.find_element(By.NAME, 'city').is_enabled()
print("City Box enabled:", city_box_ena)

driver.quit()
