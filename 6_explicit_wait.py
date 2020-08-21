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

driver.get("https://www.expedia.com/")

# Flight Button
driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/figure/div[3]/div/div/div/ul/li[2]/a").click()

time.sleep(2)  # Sleep command from Python

driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div/div[1]/div/div[1]/div/div/div/button').click()
driver.find_element_by_id("location-field-destination").send_keys("NYC")
