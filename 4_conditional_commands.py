# -*- coding: utf-8 -*-
"""
Description: Conditional commands refers to the commands to check whether certain
elements are displayed or enabled or not on a webpage.
is_displayed() and is_enabled() can be used for any type of web elements,
where as is_selected() is used only with check boxes and radio buttons.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

# To check whether username input box is displayed and enabled

usr = driver.find_element_by_name("userName")
print("Status of Username Textbox: ")
print(usr.is_displayed())  # Returns True or False based on element status
print(usr.is_enabled())  # Returns either True of False

usr.send_keys("mercury")

# To check whether password input box is displayed and enabled
psw = driver.find_element_by_name("password")
print("Status of Password Textbox: ")
print(psw.is_displayed())
print(psw.is_enabled())

psw.send_keys("mercury")

driver.find_element_by_name("login").click()

# Once login is completed to check if roundtrip radio button is selected or not on flight booking page
rund_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("Round Trip radio button status: ", rund_radio.is_selected())  # Print status of round trip radio button

driver.close()
