# -*- coding: utf-8 -*-
"""
Description: Explicit wait are based on conditions and
are applicable to particular elements unlike Implicit wait applicable to all.

it is basically used to sync between webpages that might take time to load
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()  # This will maximize the window

driver.get("https://www.yatra.com/")
# Page has by default values entered in source and destination.
# Search Page may take some time to load up the results.
# Adding Explicit wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "BE_flight_flsearch_btn")))
# Note: Extra parenthesis is added to make sure a tuple is provided as input to element_to_be_clickable
# else it will throw "__init__() takes 2 positional arguments but 3 were given" error
element.click()

time.sleep(3)

driver.quit()
