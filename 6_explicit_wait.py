# -*- coding: utf-8 -*-
"""
Description: Explicit wait are based on conditions and
are applicable to particular elements unlike Implicit wait applicable to all.

it is basically used to sync between webpages that might take time to load
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()  # This will maximize the window

driver.get("https://www.yatra.com/")

# Flight Origin City
driver.find_element_by_xpath('//*[@id="BE_flight_origin_city"]').click()
driver.find_element_by_xpath('//*[@id="BE_flight_origin_city"]').send_keys("NYC")

# Flight Destination City
driver.find_element_by_xpath('//*[@id="BE_flight_arrival_city"]').click()
driver.find_element_by_xpath('//*[@id="BE_flight_arrival_city"]').send_keys("DEL")